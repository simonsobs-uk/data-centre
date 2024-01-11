#!/usr/bin/env python

from pathlib import Path

import defopt

from souk.htcondor_helper import get_hostnames


def main(
    file: Path = Path("arch_info.template"),
    *,
    path: Path | None = None,
) -> None:
    """Generate ClassAds to collect arch_info.

    The generated ClassAds are written to the directories vanilla/ and parallel/,
    to be submitted to HTCondor.

    Args:
        file: Path to the template file.
        path: Path to write hostnames to. For inspection purposes to guarantee atomicity.
    """
    hostnames = get_hostnames()
    if path is not None:
        with path.open("w", encoding="utf-8") as f:
            for hostname in hostnames:
                f.write(f"{hostname}\n")

    with file.open(encoding="utf-8") as f:
        template = f.read()
    for universe in ["vanilla", "parallel"]:
        directory = Path(universe)
        directory.mkdir(parents=True, exist_ok=True)
        for hostname in hostnames:
            stem = f"arch_info_{hostname}"
            with open(directory / f"{stem}.ini", "w", encoding="utf-8") as f:
                f.write(
                    template.format(universe=universe, hostname=hostname, stem=stem)
                )


def cli() -> None:
    defopt.run(main, show_types=True)


if __name__ == "__main__":
    cli()
