# Contains Duplicate

## Approach
I used a hash set to keep track of the numbers that have already been seen. As I iterated through the array, I checked whether the current number was already in the set. If it was, I returned `True` because a duplicate was found. Otherwise, I added the number to the set and continued. If the loop finished without finding any duplicates, I returned `False`.

## Complexity
- Time Complexity: O(n)
- Space Complexity: O(n)

Where:
- n = number of elements in the array