# Best Time to Buy and Sell Stock

## Problem
Given an array `prices` where `prices[i]` represents the price of a stock on day `i`, find the maximum profit you can achieve by buying on one day and selling on a later day.

## Approach
- Keep track of the lowest stock price seen so far.
- For each day, calculate the profit if the stock were sold on that day.
- Update the maximum profit whenever a larger profit is found.

## Solution
The algorithm scans the array once, maintaining:
- `lowest_price`: the minimum price encountered so far.
- `max_profit`: the highest profit achievable so far.

## Complexity
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

## Key Idea
At each step:
```python
profit = current_price - lowest_price