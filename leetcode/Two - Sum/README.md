# Two Sum

## Problem
Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`.

## Approach
- Use a hash map to store numbers and their indices as you iterate through the array.
- For each number, calculate its complement:
```python
complement = target - num
