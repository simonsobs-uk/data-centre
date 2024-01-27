#!/usr/bin/env python

import sys
from pathlib import Path
from typing import TextIO

import defopt


def print_data(
    f: TextIO,
    data: list[tuple[str, str]],
    align_column: bool = False,
) -> None:
    """Print data to file."""
    max_len: int = max(len(item[0]) for item in data) if align_column else -1
    for key, value in data:
        if value:
            print(f"{key:{max_len}} = {value}", file=f)
        else:
            print(key, file=f)


def main(
    path: Path,
    *,
    align_column: bool = False,
    sort: bool = False,
    inplace: bool = False,
    output: Path | None = None,
) -> None:
    """Format INI file."""
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
    if inplace:
        output = path
    if output is None:
        print_data(sys.stdout, data, align_column=align_column)
    else:
        with output.open("w", encoding="utf-8") as f:
            print_data(f, data, align_column=align_column)


def cli() -> None:
    defopt.run(main)


if __name__ == "__main__":
    cli()
