"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        
        # Recursively calculate the depth of the left and right subtrees.
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        # The depth of the tree rooted at the current node is the maximum of
        # the depths of its left and right subtrees, plus 1 for the current node.
        return max(left_depth, right_depth) + 1

# Example usage:
# Construct the binary tree from the given input
# root = TreeNode(3)
# root.left = TreeNode(9)
# root.right = TreeNode(20)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)

# Call the maxDepth function to find the maximum depth of the tree.
# depth = maxDepth(root)
# print(depth)  # Output will be 3

"""
left_depth: This variable represents the maximum depth of the left subtree of the current node. It's the result of a recursive call to the maxDepth function on the left child of the current node.

right_depth: This variable represents the maximum depth of the right subtree of the current node. It's the result of a recursive call to the maxDepth function on the right child of the current node.

max(left_depth, right_depth): This part of the code calculates the maximum depth between the left and right subtrees. It determines which subtree is deeper and returns that maximum depth.

+ 1: Finally, we add 1 to the maximum depth of the deeper subtree to account for the current node itself. This is because we are counting the number of nodes along the path from the root to the farthest leaf node. So, we increment the depth by 1 to include the current node in the count.
"""