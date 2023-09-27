"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    # Base case: If both trees are None, they are the same.
    if not p and not q:
        return True
    
    # If one of the trees is None while the other is not, they are not the same.
    if not p or not q:
        return False
    
    # Check if the current nodes have the same value.
    if p.val != q.val:
        return False
    
    # Recursively check the left and right subtrees.
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


"""
We define the TreeNode class to represent nodes in the binary tree.

We define the isSameTree function, which takes two binary trees p and q as input.

In the isSameTree function, we first check the base case: if both p and q are None, we return True, indicating that they are the same.

Next, we check if one of the trees is None while the other is not. If this is the case, we return False, indicating that they are not the same.

If both p and q have values, we check if their values are equal. If they are not, we return False.

Finally, we recursively call isSameTree on the left and right subtrees of p and q. If both recursive calls return True, it means the entire trees are the same, so we return True.

In this example, both p and q have the same structure and values, so the isSameTree function returns True, indicating that they are the same binary trees.
"""