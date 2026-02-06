"""
PROJECT 08: DATA ANALYSIS WITH PANDAS

Pandas is the de-facto standard for data analysis in Python.
"""

import pandas as pd
import numpy as np
from typing import Dict


def create_dataframe(data: Dict) -> pd.DataFrame:
    """Create DataFrame from dictionary."""
    return pd.DataFrame(data)


def filter_dataframe(df: pd.DataFrame, column: str, value) -> pd.DataFrame:
    """Filter DataFrame rows."""
    return df[df[column] == value]


def calculate_statistics(df: pd.DataFrame, column: str) -> Dict:
    """Calculate statistics for a column."""
    return {
        'mean': df[column].mean(),
        'median': df[column].median(),
        'std': df[column].std(),
        'min': df[column].min(),
        'max': df[column].max()
    }


def group_and_aggregate(df: pd.DataFrame, group_by: str, agg_column: str) -> pd.Series:
    """Group by column and aggregate."""
    return df.groupby(group_by)[agg_column].sum()


def add_calculated_column(df: pd.DataFrame, col1: str, col2: str, new_col: str) -> pd.DataFrame:
    """Add calculated column."""
    df = df.copy()
    df[new_col] = df[col1] + df[col2]
    return df


# COMMON PANDAS OPERATIONS:
# -------------------------
# df.head()              First 5 rows
# df.info()              Column types and info
# df.describe()          Statistics
# df[column]             Select column
# df[df[col] > value]    Filter rows
# df.groupby(col)        Group data
# df.sort_values(col)    Sort
# df.fillna(value)       Handle missing data
