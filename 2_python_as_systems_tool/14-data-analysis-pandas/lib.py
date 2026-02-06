"""
Project 08: Data Analysis - Practice Stubs
"""

import pandas as pd
import numpy as np
from typing import Dict, List


def create_dataframe(data: Dict) -> pd.DataFrame:
    """
    Create a DataFrame from dictionary.

    Example:
        data = {'name': ['Alice', 'Bob'], 'age': [25, 30]}
        df = create_dataframe(data)
    """
    # TODO: Create DataFrame from dict
    pass


def filter_dataframe(df: pd.DataFrame, column: str, value) -> pd.DataFrame:
    """
    Filter DataFrame by column value.

    Example:
        filtered = filter_dataframe(df, 'age', 30)
    """
    # TODO: Filter rows where column == value
    pass


def calculate_statistics(df: pd.DataFrame, column: str) -> Dict:
    """
    Calculate basic statistics for a column.

    Returns:
        Dict with 'mean', 'median', 'std', 'min', 'max'
    """
    # TODO: Calculate statistics using pandas methods
    pass


def group_and_aggregate(df: pd.DataFrame, group_by: str, agg_column: str) -> pd.Series:
    """
    Group by column and sum another column.

    Example:
        total_sales = group_and_aggregate(df, 'category', 'sales')
    """
    # TODO: Use groupby and sum
    pass


def add_calculated_column(df: pd.DataFrame, col1: str, col2: str, new_col: str) -> pd.DataFrame:
    """
    Add new column by adding two existing columns.

    Example:
        df = add_calculated_column(df, 'price', 'tax', 'total')
    """
    # TODO: Create new column from calculation
    pass


if __name__ == "__main__":
    data = {'name': ['Alice', 'Bob'], 'age': [25, 30]}
    df = create_dataframe(data)
    print(df)
