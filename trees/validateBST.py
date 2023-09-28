"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left 
subtree
 of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def is_valid_bst(self, root, min_val=float('-inf'), max_val=float('inf')):
        # Base case: If the current node is None, it's a valid BST.
        if root is None:
            return True

        # Check if the current node's value is within the valid range.
        if not (min_val < root.val < max_val):
            return False

        # Recursively check the left and right subtrees.
        # For the left subtree, the max_val becomes the current node's value.
        # For the right subtree, the min_val becomes the current node's value.
        return (self.is_valid_bst(root.left, min_val, root.val) and
                self.is_valid_bst(root.right, root.val, max_val))

    def isValidBST(self, root: TreeNode) -> bool:
        # Start with the initial range (-infinity, +infinity).
        return self.is_valid_bst(root)

"""
The isValidBST function serves as the entry point for checking if a binary tree is a valid BST. It calls the is_valid_bst function with the initial range (-infinity to +infinity).

The is_valid_bst function checks if a binary tree rooted at root is a valid BST within the specified range (min_val to max_val).

In the recursive function:

The base case checks if the current node is None. If it is, we return True because an empty tree is a valid BST.

We check if the current node's value is within the valid range defined by min_val and max_val. If the current node's value is not within this range, it's not a valid BST, and we return False.

We recursively check the left and right subtrees, passing updated min_val and max_val values:

For the left subtree, the max_val becomes the value of the current node because all nodes in the left subtree must be less than the current node.
For the right subtree, the min_val becomes the value of the current node because all nodes in the right subtree must be greater than the current node.
If both the left and right subtrees are valid BSTs, the function returns True. Otherwise, it returns False.
"""