"""
Project 13: Monotonic Stack

Implementations of monotonic stack patterns.
"""

from typing import List


def next_greater_element(arr: List[int]) -> List[int]:
    """
    Find next greater element for each element.

    Time: O(n), Space: O(n)
    """
    n = len(arr)
    result = [-1] * n
    stack = []  # Store indices

    for i in range(n):
        while stack and arr[stack[-1]] < arr[i]:
            idx = stack.pop()
            result[idx] = arr[i]
        stack.append(i)

    return result


def largest_rectangle_histogram(heights: List[int]) -> int:
    """
    Find largest rectangular area in histogram.

    Time: O(n), Space: O(n)
    """
    stack = []
    max_area = 0
    index = 0

    while index < len(heights):
        if not stack or heights[index] >= heights[stack[-1]]:
            stack.append(index)
            index += 1
        else:
            top = stack.pop()
            width = index if not stack else index - stack[-1] - 1
            area = heights[top] * width
            max_area = max(max_area, area)

    while stack:
        top = stack.pop()
        width = index if not stack else index - stack[-1] - 1
        area = heights[top] * width
        max_area = max(max_area, area)

    return max_area


def daily_temperatures(temperatures: List[int]) -> List[int]:
    """
    Calculate days until warmer temperature.

    Time: O(n), Space: O(n)
    """
    n = len(temperatures)
    result = [0] * n
    stack = []

    for i in range(n):
        while stack and temperatures[stack[-1]] < temperatures[i]:
            idx = stack.pop()
            result[idx] = i - idx
        stack.append(i)

    return result


def stock_span(prices: List[int]) -> List[int]:
    """
    Calculate stock span (consecutive days with price <= current).

    Time: O(n), Space: O(n)
    """
    n = len(prices)
    span = [1] * n
    stack = []

    for i in range(n):
        while stack and prices[stack[-1]] <= prices[i]:
            stack.pop()

        span[i] = i + 1 if not stack else i - stack[-1]
        stack.append(i)

    return span


if __name__ == "__main__":
    print("Monotonic Stack Demonstrations")
    print("=" * 60)

    arr = [4, 5, 2, 10, 8]
    print(f"\n1. Next Greater Element: {arr}")
    print(f"   Result: {next_greater_element(arr)}")

    heights = [2, 1, 5, 6, 2, 3]
    print(f"\n2. Largest Rectangle: {heights}")
    print(f"   Max Area: {largest_rectangle_histogram(heights)}")

    temps = [73, 74, 75, 71, 69, 72, 76, 73]
    print(f"\n3. Daily Temperatures: {temps}")
    print(f"   Days: {daily_temperatures(temps)}")

    prices = [100, 80, 60, 70, 60, 75, 85]
    print(f"\n4. Stock Span: {prices}")
    print(f"   Span: {stock_span(prices)}")

    print("\n" + "=" * 60)
