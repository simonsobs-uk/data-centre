#!/usr/bin/env python

from __future__ import annotations

from pathlib import Path

import defopt
import pandas as pd

from souk.system.arch_info import Systems

pd.set_option('future.no_silent_downcasting', True)


def merge_df(
    df_left: pd.DataFrame,
    df_right: pd.DataFrame,
) -> pd.DataFrame:
    """
    Merges two pandas DataFrames by their indices using an outer join, handling duplicate columns.

    This function takes two pandas DataFrames, `df_left` and `df_right`, and performs an outer join
    on their indices. It resolves duplicate columns by filling null values in the original columns
    with values from the duplicate columns. Duplicate columns are identified by a "_duplicate" suffix.
    After filling, these duplicate columns are dropped from the final DataFrame.

    Parameters:
    df_left (pd.DataFrame): The left DataFrame to be merged.
    df_right (pd.DataFrame): The right DataFrame to be merged.

    Returns:
    pd.DataFrame: A merged DataFrame with resolved duplicates.

    Example:
    >>> df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]}, index=[0, 1])
    >>> df2 = pd.DataFrame({'B': [5, 6], 'C': [7, 8]}, index=[0, 1])
    >>> merge_df(df1, df2)
       A  B  C
    0  1  3  7
    1  2  4  8

    Note:
    - The function assumes that the indices of the DataFrames are meaningful for the merge.
    - If the same column name exists in both DataFrames, the function prefers the values from `df_left`.
    """
    columns: set[str] = set(df_left.columns.tolist()) | set(df_right.columns.tolist())
    df_merged = df_left.merge(
        df_right,
        how="outer",
        left_index=True,
        right_index=True,
        suffixes=("", "_duplicate"),
    )

    for col_other in df_merged.columns:
        if col_other not in columns:
            col = col_other[:-10]
            df_merged[col] = df_merged[col].fillna(df_merged[col_other])
            df_merged.drop(columns=[col_other], inplace=True)
    return df_merged


def main(
    path: Path = Path("systems.csv"),
    *,
    universes: list[str] = ["vanilla", "parallel"],
    simplified: bool = False,
) -> None:
    dfs = []
    for universe in universes:
        paths = Path(universe).glob("*.yml")
        systems = Systems.from_yaml(*paths)
        df = systems.dataframe_simplified() if simplified else systems.dataframe
        df[f"{universe} universe"] = True
        dfs.append(df)

    df_merged = merge_df(*dfs)
    for universe in universes:
        df_merged[f"{universe} universe"] = df_merged[f"{universe} universe"].fillna(False).infer_objects(copy=False)

    if simplified:
        # cast
        for key in (
            "No. of sockets",
            "Total no. of logical cores",
            "Total no. of physical cores",
            "Total memory (GiB)",
            "Total swap (GiB)",
        ):
            df_merged[key] = df_merged[key].astype(int)
    if path.suffix == ".csv":
        df_merged.to_csv(path)
    elif path.suffix == ".html":
        df_merged.to_html(path)
    else:
        raise ValueError(f"Unknown file extension: {path.suffix}")


def cli() -> None:
    defopt.run(main, show_types=True)


if __name__ == "__main__":
    cli()
