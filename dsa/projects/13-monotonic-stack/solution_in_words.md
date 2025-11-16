# Project 13: Monotonic Stack - Solution Explained

## Concept Overview

A **Monotonic Stack** maintains elements in monotonic (strictly increasing or decreasing) order. When a new element violates the order, we pop elements until order is restored.

**Pattern:** For "next greater element" problems, use a decreasing monotonic stack.

## Problem Solutions

### 1. Next Greater Element
**Approach:** Iterate through array. For each element, pop all smaller elements from stack (they found their next greater). Push current element.
**Complexity:** O(n) - each element pushed/popped once

### 2. Largest Rectangle in Histogram
**Approach:** For each bar, find how far left and right it can extend. Use stack to find boundaries in O(n).
**Key Insight:** When we pop a bar, we know its boundaries.
**Complexity:** O(n)

### 3. Daily Temperatures
**Approach:** Monotonic stack storing indices. When we find warmer day, pop and calculate difference.
**Complexity:** O(n)

### 4. Stock Span
**Approach:** Stack stores indices of days. Span = current day - last day with higher price.
**Complexity:** O(n)

## Key Takeaways
- Monotonic stacks reduce O(n²) to O(n)
- Each element pushed and popped at most once
- Perfect for "next greater/smaller" problems
- Used in: histogram problems, span problems, visibility problems
