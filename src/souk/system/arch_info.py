#!/usr/bin/env python

from __future__ import annotations

import json
import platform
import subprocess
from dataclasses import dataclass
from functools import cached_property
from io import StringIO
from pathlib import Path
from typing import TYPE_CHECKING

import archspec.cpu
import cpuinfo
import defopt
import pandas as pd
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
    def host(self) -> archspec.cpu.Host:
        return archspec.cpu.host()

    @property
    def host_optimization_flags(self) -> str:
        return self.host.optimization_flags("gcc", 12)

    @property
    def host_generic(self) -> archspec.cpu.Generic:
        return self.host.generic

    @property
    def host_generic_optimization_flags(self) -> str:
        return self.host_generic.optimization_flags("gcc", 12)

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
        data["archspec.cpu.host"] = self.host.to_dict()
        data["archspec.cpu.host.optimization_flags.gcc_12"] = (
            self.host_optimization_flags
        )
        data["archspec.cpu.host.generic"] = self.host_generic.to_dict()
        data["archspec.cpu.host.generic.optimization_flags.gcc_12"] = (
            self.host_generic_optimization_flags
        )
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
        ruamel_yaml = YAML()
        ruamel_yaml.representer.add_representer(None, generic_represent_undefined)
        ruamel_yaml.default_flow_style = False
        ruamel_yaml.dump(data, res)
        return res.getvalue()

    def write_yaml(self, path: Path) -> None:
        path = Path(path)
        path.write_text(self.to_yaml(), encoding="utf-8")

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> System:
        self = cls()
        self.uname = data["uname"]
        self.host = archspec.cpu.Microarchitecture.from_dict(data["archspec.cpu.host"])
        self.physical_cpu_count = data["psutil.cpu_count.physical"]
        self.logical_cpu_count = data["psutil.cpu_count.logical"]
        self.cpuinfo = data["cpuinfo"]
        self.system_cpu_info = data["system_cpu_info"]
        self.total_memory = data["psutil.virtual_memory.total"]
        self.total_swap = data["psutil.swap_memory.total"]
        self.active_interfaces = data["psutil.net_if_stats"]
        return self

    @classmethod
    def from_yaml(cls, path: Path) -> System:
        path = Path(path)
        data = YAML().load(path.read_text(encoding="utf-8"))
        return cls.from_dict(data)


@dataclass
class Systems:
    """A class of multiple System."""

    systems: list[System]

    @classmethod
    def from_yaml(cls, *paths: Path) -> Systems:
        return cls([System.from_yaml(path) for path in paths])

    @property
    def data(self) -> list[dict[str, Any]]:
        return [system.data for system in self.systems]

    @cached_property
    def dataframe(self) -> pd.DataFrame:
        df = pd.json_normalize(self.data)
        df.set_index("uname.node", inplace=True)
        df.sort_index(inplace=True)
        return df

    def dataframe_simplified(
        self,
        columns: tuple[str, ...] = (
            "cpuinfo.brand_raw",
            "archspec.cpu.host.vendor",
            "archspec.cpu.host.name",
            "archspec.cpu.host.generic.name",
            "system_cpu_info.Socket(s)",
            "psutil.cpu_count.logical",
            "psutil.cpu_count.physical",
            "psutil.virtual_memory.total",
            "psutil.swap_memory.total",
        ),
    ) -> pd.DataFrame:
        df = self.dataframe[list(columns)].copy()
        df.index.name = "hostname"
        # cast type
        for key in (
            "psutil.cpu_count.physical",
            "psutil.cpu_count.logical",
            "system_cpu_info.Socket(s)",
            "psutil.virtual_memory.total",
            "psutil.swap_memory.total",
        ):
            df[key] = df[key].astype(int)
        # to GiB
        for key in ("psutil.virtual_memory.total", "psutil.swap_memory.total"):
            df[key] = df[key] / 1024**3
        df.rename(
            columns={
                "cpuinfo.brand_raw": "CPU model",
                "archspec.cpu.host.vendor": "CPU vendor",
                "archspec.cpu.host.name": "CPU generation",
                "archspec.cpu.host.generic.name": "CPU microarchitecture",
                "system_cpu_info.Socket(s)": "No. of sockets",
                "psutil.cpu_count.logical": "Total no. of logical cores",
                "psutil.cpu_count.physical": "Total no. of physical cores",
                "psutil.virtual_memory.total": "Total memory (GiB)",
                "psutil.swap_memory.total": "Total swap (GiB)",
            },
            inplace=True,
        )
        # round
        for key in ("Total memory (GiB)", "Total swap (GiB)"):
            df[key] = df[key].round(0).astype(int)
        return df

    def to_csv(
        self,
        path: Path,
        simplified: bool = False,
    ) -> None:
        if simplified:
            self.dataframe_simplified().to_csv(path)
        else:
            self.dataframe.to_csv(path)


def arch_info(
    *,
    path: Path = Path(f"arch_info_{platform.node()}.yml"),
) -> None:
    """Writes the system information to the given path in YAML."""
    system = System()
    system.write_yaml(path)


def collect_arch_info(
    *paths: Path,
    output: Path = Path("arch_info.csv"),
    simplified: bool = False,
) -> None:
    """Collects the system information collected by arch-info and writes it to the CSV file."""
    systems = Systems.from_yaml(*paths)
    systems.to_csv(output, simplified=simplified)


def cli() -> None:
    """The command line interface for arch_info."""
    defopt.run(
        [arch_info, collect_arch_info],
        strict_kwonly=False,
        show_defaults=True,
        show_types=True,
    )


if __name__ == "__main__":
    cli()
