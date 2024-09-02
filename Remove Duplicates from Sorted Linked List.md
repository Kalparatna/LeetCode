
# Remove Duplicates from Sorted Linked List

## Description

This project implements a solution to remove duplicates from a sorted singly-linked list. Given the head of a sorted linked list, the goal is to delete all duplicates such that each element appears only once. The linked list is returned sorted as well.

## Problem Statement

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

### Example 1:

- **Input:** `head = [1,1,2]`
- **Output:** `[1,2]`

### Example 2:

- **Input:** `head = [1,1,2,3,3]`
- **Output:** `[1,2,3]`

## Implementation

The solution is implemented in Python using a class-based approach.

### ListNode Class

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

### Solution Class

```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head

        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return head
```

### Explanation

- **ListNode class:** Represents a node in a singly-linked list with `val` and `next` attributes.
- **Solution class:** Contains the `deleteDuplicates` method that removes duplicates from the sorted linked list.
  - The method iterates through the list using the `cur` pointer.
  - If two consecutive nodes have the same value, the duplicate node is skipped by updating the `next` pointer.
  - The method returns the head of the modified linked list.

### Complexity Analysis

- **Time Complexity:** O(n), where `n` is the number of nodes in the linked list. Each node is visited exactly once.
- **Space Complexity:** O(1), since we are not using any extra space besides the pointers.

## Usage

To use this solution, you can create instances of `ListNode` and pass the head of the linked list to the `deleteDuplicates` method in the `Solution` class.

### Example Usage

```python
# Helper function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    cur = head
    for val in values[1:]:
        cur.next = ListNode(val)
        cur = cur.next
    return head

# Helper function to print the linked list
def print_linked_list(head):
    cur = head
    while cur:
        print(cur.val, end=" -> ")
        cur = cur.next
    print("None")

# Example
head = create_linked_list([1, 1, 2, 3, 3])
solution = Solution()
head = solution.deleteDuplicates(head)
print_linked_list(head)
```

### Output

For the input `[1, 1, 2, 3, 3]`, the output will be:

```
1 -> 2 -> 3 -> None
```
