#!/usr/bin/env python

from __future__ import annotations

import json
import platform
import subprocess
from functools import cached_property
from io import StringIO
from pathlib import Path
from typing import TYPE_CHECKING

import archspec
import archspec.cpu
import cpuinfo
import defopt
import psutil
from ruamel.yaml import YAML

if TYPE_CHECKING:
    from typing import Any

    from ruamel.yaml.nodes import Node
    from ruamel.yaml.representer import BaseRepresenter


def sort_nested_dicts(obj: Any) -> Any:
    """
    Recursively sorts nested dictionaries in the given object.

    :param obj: A dictionary or a JSON-like object with potentially nested dictionaries.
    :return: A new object with all nested dictionaries sorted by their keys.
    """
    if isinstance(obj, dict):
        # Sort the dictionary and apply the same function to its values
        return dict(sorted(obj.items(), key=lambda x: x[0]))
    elif isinstance(obj, list):
        # Apply the function to each element in the list
        return [sort_nested_dicts(element) for element in obj]
    else:
        # Return the object as is if it's not a dict or list
        return obj


def _run_lscpu() -> str:
    """Executes the lscpu command and returns its output."""
    result = subprocess.run("lscpu", text=True, check=True, capture_output=True)
    return result.stdout


def _parse_lscpu(stdout: str) -> dict[str, str]:
    """Parses the output of lscpu into a dictionary."""
    return {
        key.strip(): value.strip()
        for line in stdout.split("\n")
        if line.strip()
        for key, value in [line.split(":", 1)]
    }


def lscpu() -> dict[str, str]:
    return _parse_lscpu(_run_lscpu())


def system_profiler() -> dict[str, str]:
    """Returns the output of system_profiler as a dictionary."""
    result = subprocess.run(
        ["system_profiler", "-json", "SPHardwareDataType"],
        text=True,
        check=True,
        capture_output=True,
    )
    return json.loads(result.stdout)["SPHardwareDataType"][0]


def field_to_dict(obj: Any) -> dict[str, Any]:
    return {field: getattr(obj, field) for field in obj._fields}


def uname() -> dict[str, str]:
    return field_to_dict(platform.uname())


def get_active_interfaces() -> dict[str, dict[str, Any]]:
    interface_stats = psutil.net_if_stats()
    active_interfaces = {
        intf: field_to_dict(stats)
        for intf, stats in interface_stats.items()
        if stats.speed > 0
    }
    return active_interfaces


def generic_represent_undefined(representer: BaseRepresenter, data: Any) -> Node:
    """
    Generic representer for undefined objects.
    Represents the object using its str or repr.
    """
    return representer.represent_scalar("tag:yaml.org,2002:str", repr(data))


class System:
    """A class that contains information about the system."""

    @cached_property
    def uname(self) -> dict[str, str]:
        return uname()

    @cached_property
    def _host(self) -> archspec.cpu.Host:
        return archspec.cpu.host()

    @cached_property
    def host(self) -> dict[str, Any]:
        return self._host.to_dict()

    @cached_property
    def host_optimization_flags(self) -> str:
        return self._host.optimization_flags("gcc", 12)

    @cached_property
    def _host_generic(self) -> archspec.cpu.Generic:
        return self._host.generic

    @cached_property
    def host_generic(self) -> dict[str, Any]:
        return self._host_generic.to_dict()

    @cached_property
    def host_generic_optimization_flags(self) -> str:
        return self._host_generic.optimization_flags("gcc", 12)

    @cached_property
    def physical_cpu_count(self) -> int:
        return psutil.cpu_count(logical=False)

    @cached_property
    def logical_cpu_count(self) -> int:
        return psutil.cpu_count(logical=True)

    @cached_property
    def cpuinfo(self) -> dict[str, Any]:
        return cpuinfo.get_cpu_info()

    @cached_property
    def system_cpu_info(self) -> dict[str, str]:
        if (system := platform.system()) == "Linux":
            return lscpu()
        elif system == "Darwin":
            return system_profiler()
        else:
            raise NotImplementedError(
                f"system_cpu_info is not implemented for {system}"
            )

    @cached_property
    def total_memory(self) -> int:
        return psutil.virtual_memory().total

    @cached_property
    def total_swap(self) -> int:
        return psutil.swap_memory().total

    @cached_property
    def active_interfaces(self) -> dict[str, dict[str, Any]]:
        return get_active_interfaces()

    @property
    def data(self) -> dict[str, Any]:
        data: dict[str, Any] = {}
        data["uname"] = self.uname
        data["archspec.cpu.host"] = self.host
        data[
            "archspec.cpu.host.optimization_flags.gcc_12"
        ] = self.host_optimization_flags
        data["archspec.cpu.host.generic"] = self.host_generic
        data[
            "archspec.cpu.host.generic.optimization_flags.gcc_12"
        ] = self.host_generic_optimization_flags
        data["psutil.cpu_count.physical"] = self.physical_cpu_count
        data["psutil.cpu_count.logical"] = self.logical_cpu_count
        data["cpuinfo"] = self.cpuinfo
        data["system_cpu_info"] = self.system_cpu_info
        data["psutil.virtual_memory.total"] = self.total_memory
        data["psutil.swap_memory.total"] = self.total_swap
        data["psutil.net_if_stats"] = self.active_interfaces
        return sort_nested_dicts(data)

    def to_yaml(self) -> str:
        res = StringIO()
        data = self.data
        ruamel_yaml = YAML(typ="safe")
        ruamel_yaml.representer.add_representer(None, generic_represent_undefined)
        ruamel_yaml.default_flow_style = False
        ruamel_yaml.dump(data, res)
        return res.getvalue()

    def write_yaml(self, path: Path, **kwargs) -> None:
        path = Path(path)
        path.write_text(self.to_yaml(**kwargs), encoding="utf-8")

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> System:
        self = cls()
        self.uname = data["uname"]
        self.host = data["archspec.cpu.host"]
        self.host_optimization_flags = data[
            "archspec.cpu.host.optimization_flags.gcc_12"
        ]
        self.host_generic = data["archspec.cpu.host.generic"]
        self.host_generic_optimization_flags = data[
            "archspec.cpu.host.generic.optimization_flags.gcc_12"
        ]
        self.physical_cpu_count = data["psutil.cpu_count.physical"]
        self.logical_cpu_count = data["psutil.cpu_count.logical"]
        self.cpuinfo = data["cpuinfo"]
        self.system_cpu_info = data["system_cpu_info"]
        self.total_memory = data["psutil.virtual_memory.total"]
        self.total_swap = data["psutil.swap_memory.total"]
        self.active_interfaces = data["psutil.net_if_stats"]
        return self


def arch_info(
    *,
    path: Path = Path(f"arch_info_{platform.node()}.yaml"),
) -> None:
    """Writes the system information to the given path in YAML."""
    system = System()
    system.write_yaml(path)


def cli() -> None:
    """The command line interface for arch_info."""
    defopt.run(arch_info, strict_kwonly=False, show_defaults=True, show_types=True)


if __name__ == "__main__":
    cli()
