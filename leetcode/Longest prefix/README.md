# Longest Common Prefix

## Approach
I used the first string as the initial prefix and compared it with every other string in the array. If a string did not start with the current prefix, I repeatedly removed the last character from the prefix until it matched. After checking all strings, the remaining prefix was returned as the longest common prefix.

## Complexity
- Time Complexity: O(n × m)
- Space Complexity: O(1)

Where:
- n = number of strings
- m = length of the prefix