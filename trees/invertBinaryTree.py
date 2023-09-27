"""
Given the root of a binary tree, invert the tree, and return its root. 
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:


Input: root = [2,1,3]
Output: [2,3,1] The number of nodes in the tree is in the range [0, 100].
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root):
    # Base case: If the root is None, return None.
    if root is None:
        return None

    # Swap the left and right subtrees recursively.
    root.left, root.right = invertTree(root.right), invertTree(root.left)

    return root

# Example usage:

# Create the binary tree from the given input
# root = TreeNode(4)
# root.left = TreeNode(2)
# root.right = TreeNode(7)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(3)
# root.right.left = TreeNode(6)
# root.right.right = TreeNode(9)

# Call the invertTree function to invert the tree.
# inverted_root = invertTree(root)

# The 'inverted_root' now contains the inverted tree, and you can traverse it as needed.

"""
The function takes the root of the binary tree as input.

In the base case, if the root is None, we return None because there's nothing to invert.

For a non-empty tree, we swap the left and right subtrees of the current node by recursively calling invertTree on the left and right children. We use a Pythonic way of swapping values using simultaneous assignment: root.left, root.right = invertTree(root.right), invertTree(root.left).

Finally, we return the root of the inverted tree.

We start with the root node, which has a value of 4.

Since the root is not None, we proceed to swap its left and right subtrees.

The left subtree (node with value 2) has children 1 and 3.
The right subtree (node with value 7) has children 6 and 9.
We swap the left and right subtrees of the root, resulting in the following:

"""