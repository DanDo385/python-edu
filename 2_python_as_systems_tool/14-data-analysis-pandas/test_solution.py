"""
Project 08: Data Analysis - Tests
"""

import pytest
import pandas as pd
import numpy as np
from solution import (
    create_dataframe,
    filter_dataframe,
    calculate_statistics,
    group_and_aggregate,
    add_calculated_column
)


class TestCreateDataFrame:
    def test_create_simple_dataframe(self):
        data = {'name': ['Alice', 'Bob'], 'age': [25, 30]}
        df = create_dataframe(data)
        assert len(df) == 2
        assert list(df.columns) == ['name', 'age']


class TestFilterDataFrame:
    def test_filter_by_value(self):
        df = pd.DataFrame({'name': ['Alice', 'Bob', 'Charlie'], 'age': [25, 30, 25]})
        filtered = filter_dataframe(df, 'age', 25)
        assert len(filtered) == 2
        assert 'Alice' in filtered['name'].values


class TestCalculateStatistics:
    def test_statistics(self):
        df = pd.DataFrame({'values': [1, 2, 3, 4, 5]})
        stats = calculate_statistics(df, 'values')
        assert stats['mean'] == 3.0
        assert stats['min'] == 1
        assert stats['max'] == 5


class TestGroupAndAggregate:
    def test_groupby_sum(self):
        df = pd.DataFrame({
            'category': ['A', 'B', 'A', 'B'],
            'sales': [10, 20, 30, 40]
        })
        result = group_and_aggregate(df, 'category', 'sales')
        assert result['A'] == 40
        assert result['B'] == 60


class TestAddCalculatedColumn:
    def test_add_column(self):
        df = pd.DataFrame({'price': [10, 20], 'tax': [1, 2]})
        result = add_calculated_column(df, 'price', 'tax', 'total')
        assert 'total' in result.columns
        assert list(result['total']) == [11, 22]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
