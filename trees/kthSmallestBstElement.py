"""
Given the root of a binary search tree, and an integer k, 
return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Input: root = [3,1,4,null,2], k = 1
Output: 1
Example 2:


Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # Initialize a list to store visited nodes during in-order traversal.
        visited = []

        # Helper function to perform in-order traversal and populate the visited list.
        def in_order_traversal(node):
            if not node:
                return
            # Recursively traverse the left subtree.
            in_order_traversal(node.left)
            # Append the current node's value to the visited list.
            visited.append(node.val)
            # Recursively traverse the right subtree.
            in_order_traversal(node.right)

        # Start the in-order traversal from the root node.
        in_order_traversal(root)

        # Return the kth smallest value from the visited list (1-indexed).
        return visited[k - 1]

"""
We define a class TreeNode to represent nodes in the binary search tree (BST).

In the kthSmallest function, we initialize an empty list visited to store the values of visited nodes during the in-order traversal.

We define a helper function in_order_traversal to perform the in-order traversal of the BST. In an in-order traversal, we visit nodes in ascending order.

Inside the in_order_traversal function:

If the current node is None, we return, as there are no more nodes to visit.
We recursively traverse the left subtree.
We append the current node's value to the visited list.
We recursively traverse the right subtree.
We start the in-order traversal from the root node by calling in_order_traversal(root).

After the traversal is complete, the visited list contains all the values of the nodes in ascending order.

Finally, we return the kth smallest value from the visited list, which is accessed using visited[k - 1]. The result is 1-indexed.

Let's consider the examples:

Example 1:
Input: root = [3, 1, 4, None, 2], k = 1

The in-order traversal of the BST [3, 1, 4, None, 2] is [1, 2, 3, 4]. The 1st smallest value is 1, so the output is 1.

Example 2:
Input: root = [5, 3, 6, 2, 4, None, None, 1], k = 3

The in-order traversal of the BST [5, 3, 6, 2, 4, None, None, 1] is [1, 2, 3, 4, 5, 6]. The 3rd smallest value is 3, so the output is 3.
"""