"""
Project 08: Data Analysis - Demo
"""

import pandas as pd
import numpy as np
from solution import (
    create_dataframe,
    filter_dataframe,
    calculate_statistics,
    group_and_aggregate,
    add_calculated_column
)


def demo_create():
    print("=" * 70)
    print("DEMO 1: Create DataFrame")
    print("=" * 70)

    data = {
        'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'age': [25, 30, 35, 25],
        'salary': [50000, 60000, 70000, 55000]
    }

    df = create_dataframe(data)
    print(df)
    print()


def demo_filter():
    print("=" * 70)
    print("DEMO 2: Filter Data")
    print("=" * 70)

    df = pd.DataFrame({
        'name': ['Alice', 'Bob', 'Charlie'],
        'age': [25, 30, 25],
        'city': ['NYC', 'LA', 'NYC']
    })

    filtered = filter_dataframe(df, 'city', 'NYC')
    print("People in NYC:")
    print(filtered)
    print()


def demo_statistics():
    print("=" * 70)
    print("DEMO 3: Calculate Statistics")
    print("=" * 70)

    df = pd.DataFrame({'scores': [85, 90, 78, 92, 88]})
    stats = calculate_statistics(df, 'scores')

    for key, value in stats.items():
        print(f"{key}: {value:.2f}")
    print()


def demo_groupby():
    print("=" * 70)
    print("DEMO 4: Group and Aggregate")
    print("=" * 70)

    df = pd.DataFrame({
        'category': ['Electronics', 'Clothing', 'Electronics', 'Clothing'],
        'product': ['Laptop', 'Shirt', 'Mouse', 'Pants'],
        'sales': [1000, 50, 25, 75]
    })

    total_by_category = group_and_aggregate(df, 'category', 'sales')
    print("Total sales by category:")
    print(total_by_category)
    print()


def demo_calculated_column():
    print("=" * 70)
    print("DEMO 5: Add Calculated Column")
    print("=" * 70)

    df = pd.DataFrame({
        'product': ['Laptop', 'Mouse'],
        'price': [1000, 25],
        'tax': [100, 2.5]
    })

    result = add_calculated_column(df, 'price', 'tax', 'total')
    print(result)
    print()


def main():
    print("\n📊" * 35)
    print("  PROJECT 08: DATA ANALYSIS WITH PANDAS")
    print("📊" * 35)
    print()

    demo_create()
    demo_filter()
    demo_statistics()
    demo_groupby()
    demo_calculated_column()

    print("=" * 70)
    print("Key Takeaways:")
    print("1. DataFrames are 2D labeled data structures")
    print("2. Filter with boolean indexing: df[df[col] > value]")
    print("3. groupby() enables powerful aggregations")
    print("4. Pandas makes data analysis intuitive and fast")
    print()


if __name__ == "__main__":
    main()
