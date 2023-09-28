"""
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

 

Example 1:


Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
Example 2:


Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
 

Constraints:

The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-104 <= root.val <= 104
-104 <= subRoot.val <= 104
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        # Helper function to compare two trees for equality
        def isSameTree(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            return (
                node1.val == node2.val and
                isSameTree(node1.left, node2.left) and
                isSameTree(node1.right, node2.right)
            )
        
        # Base case: If root is None, it's not a valid subtree.
        if not root:
            return False
        
        # Check if the current root node matches the subRoot.
        if isSameTree(root, subRoot):
            return True
        
        # Recursively check the left and right subtrees.
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

"""
The isSubtree function takes two binary tree nodes, root and subRoot, and returns True if there is a subtree in root that matches subRoot.

There is a helper function isSameTree that checks if two trees are identical. It recursively compares the values of nodes in the trees.

The base case checks if root is None. If root is None, it's not a valid subtree, so we return False.

We then check if the current root node matches the subRoot by calling isSameTree(root, subRoot). If they are the same, we return True.

If the current root node doesn't match subRoot, we recursively check the left and right subtrees by calling self.isSubtree(root.left, subRoot) and self.isSubtree(root.right, subRoot).

We return True if either the left or right subtree contains a matching subtree, indicating that there is a subtree in root with the same structure and node values as subRoot.

You can use this isSubtree function to check if root contains a subtree that matches subRoot, as shown in the provided examples.
"""