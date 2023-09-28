"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

Example 1:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [2,1], p = 2, q = 1
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the BST.
"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Base case: If the root is None, return None.
        if not root:
            return None

        # If both p and q are greater than the current root's value,
        # the LCA must be in the right subtree.
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        # If both p and q are less than the current root's value,
        # the LCA must be in the left subtree.
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        # If one of p or q is equal to the current root's value or
        # one is greater and the other is less, then the current root
        # is the LCA according to the LCA definition.
        else:
            return root

"""
We define a class TreeNode to represent nodes in the binary search tree (BST).

In the lowestCommonAncestor function, we take the root node of the BST and the two target nodes p and q as input.

In the recursive function:

The base case checks if the current root is None. If it is, we return None because there's no common ancestor to be found.

We compare the values of p and q with the current root's value:

If both p and q are greater than the current root's value, it means both nodes are in the right subtree, so we recursively search in the right subtree.
If both p and q are less than the current root's value, it means both nodes are in the left subtree, so we recursively search in the left subtree.
If one of p or q is equal to the current root's value or one is greater and the other is less, then the current root is the lowest common ancestor according to the LCA definition.
Finally, we return the LCA node.

Let's consider the examples:

Example 1:
Input: root = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], p = 2, q = 8

The LCA of nodes 2 and 8 is 6.

Example 2:
Input: root = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], p = 2, q = 4

The LCA of nodes 2 and 4 is 2.

Example 3:
Input: root = [2, 1], p = 2, q = 1

The LCA of nodes 2 and 1 is 2.

The code efficiently navigates the BST to find the lowest common ancestor based on the values of p and q.
"""