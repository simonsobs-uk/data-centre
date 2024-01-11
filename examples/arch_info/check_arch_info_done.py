#!/usr/bin/env python

from pathlib import Path

import defopt


def main(
    path: Path = Path("hostnames.txt"),
) -> None:
    """Check arch_info jobs finished.

    Args:
        path: Path to hostnames.
    """
    hostnames = path.read_text(encoding="utf-8").strip().split("\n")
    for universe in ["vanilla", "parallel"]:
        directory = Path(universe)
        for hostname in hostnames:
            stem = f"arch_info_{hostname}"
            file_expected = directory / f"{stem}.yml"
            if not file_expected.exists():
                print(f"{hostname}\tnot finished in {universe} universe")


def cli() -> None:
    defopt.run(main, show_types=True)


if __name__ == "__main__":
    cli()
