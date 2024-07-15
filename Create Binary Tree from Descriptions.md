# Problem: Create Binary Tree from Descriptions

## Problem Statement

You are given a 2D integer array `descriptions` where `descriptions[i] = [parent_i, child_i, isLeft_i]` indicates that `parent_i` is the parent of `child_i` in a binary tree of unique values. Furthermore,

- If `isLeft_i == 1`, then `child_i` is the left child of `parent_i`.
- If `isLeft_i == 0`, then `child_i` is the right child of `parent_i`.

Construct the binary tree described by `descriptions` and return its root.

The test cases will be generated such that the binary tree is valid.

### Examples

#### Example 1

Input: descriptions = `[[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]`

Output: `[50,20,80,15,17,19]`

Explanation: The root node is the node with value 50 since it has no parent. The resulting binary tree is shown in the diagram.

#### Example 2

Input: descriptions = `[[1,2,1],[2,3,0],[3,4,1]]`

Output: `[1,2,null,null,3,4]`

Explanation: The root node is the node with value 1 since it has no parent. The resulting binary tree is shown in the diagram.

## Solution

```python


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        node_map = {}
        children = set()

        # Step 1: Create nodes and build relationships
        for parent, child, is_left in descriptions:
            if parent not in node_map:
                node_map[parent] = TreeNode(parent)
            if child not in node_map:
                node_map[child] = TreeNode(child)

            if is_left:
                node_map[parent].left = node_map[child]
            else:
                node_map[parent].right = node_map[child]

            children.add(child)

        # Step 2: Identify the root node
        for parent, _, _ in descriptions:
            if parent not in children:
                return node_map[parent]
