# Merge Two Sorted Lists

## Approach

To solve this problem, I used a dummy node and a pointer called `current` to build the merged linked list.

1. Compare the values of the current nodes in both lists.
2. Attach the smaller node to the merged list.
3. Move the pointer of the list from which the node was taken.
4. Move the `current` pointer forward.
5. Repeat until one list is exhausted.
6. Attach the remaining nodes from the non-empty list.
7. Return `dummy.next`, which points to the head of the merged list.

## Time Complexity
- **O(n + m)**, where `n` and `m` are the lengths of the two linked lists.

## Space Complexity
- **O(1)**, since the existing nodes are reused and no extra list is created.