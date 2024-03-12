#!/usr/bin/env python

from glob import glob
from pathlib import Path

import defopt


def ini_formatter(
    path: Path,
    *,
    align_column: bool = False,
    sort: bool = False,
) -> None:
    """Format INI file inplace.

    param: path: Path to INI file.
    param: align_column: Align column.
    param: sort: Sort keys
    """
    data: list[tuple[str, str]] = []
    with path.open(encoding="utf-8") as f:
        for line in f:
            temp = line.split("=", 1)
            if len(temp) == 2:
                data.append((temp[0].strip(), temp[1].strip()))
            else:
                data.append((temp[0].strip(), ""))
    if sort:
        # filter empty lines
        data = [line for line in data if line != ("", "")]
        data.sort(key=lambda x: x[0])
    max_len: int = max(len(item[0]) for item in data if item[1]) if align_column else 0
    with path.open("w", encoding="utf-8") as f:
        for key, value in data:
            if value:
                print(f"{key:{max_len}} = {value}", file=f)
            else:
                print(key, file=f)


def main(
    glob_pattern: str,
    *,
    align_column: bool = False,
    sort: bool = False,
) -> None:
    """Format INI file inplace.

    param: glob_pattern: Glob pattern to match files.
    param: align_column: Align column.
    param: sort: Sort keys
    """
    for p in glob(glob_pattern, recursive=True):
        ini_formatter(
            Path(p),
            align_column=align_column,
            sort=sort,
        )


def cli() -> None:
    defopt.run(main)


if __name__ == "__main__":
    cli()
