#!/usr/bin/env python

"""Prints a string with the given arguments.

Usage:
    arg_string path/to/template.txt arg1=value1 arg2=value2
"""


from __future__ import annotations

from pathlib import Path

import fire


def arg_string(path: Path, **kwargs: str) -> None:
    """Prints a string with the given arguments."""
    path = Path(path)

    with path.open(encoding="utf-8") as f:
        template = f.read()
    print(template.format(**kwargs))


def cli() -> None:
    fire.Fire(arg_string)


if __name__ == "__main__":
    cli()
