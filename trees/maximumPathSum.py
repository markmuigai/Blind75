"""
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path. Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6. Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
 

Constraints:

The number of nodes in the tree is in the range [1, 3 * 104].
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # Initialize a variable to store the maximum path sum.
        self.max_sum = float('-inf')
        
        # Helper function to calculate the maximum path sum starting from a node.
        def maxPathSumFromNode(node):
            if not node:
                return 0
            
            # Calculate the maximum path sum for the left and right subtrees.
            left_sum = max(maxPathSumFromNode(node.left), 0)
            right_sum = max(maxPathSumFromNode(node.right), 0)
            
            # Update the maximum path sum overall by considering the path through the current node.
            self.max_sum = max(self.max_sum, left_sum + right_sum + node.val)
            
            # Return the maximum path sum starting from the current node.
            return max(left_sum, right_sum) + node.val
        
        # Start the recursion from the root node.
        maxPathSumFromNode(root)
        
        return self.max_sum

"""
We define the TreeNode class to represent nodes in the binary tree.

In the maxPathSum function, we initialize a variable self.max_sum to negative infinity to store the maximum path sum overall.

We define a helper function maxPathSumFromNode that calculates the maximum path sum starting from a given node. This function returns the maximum path sum starting from the node.

In the helper function, we handle the base case: If the node is None, we return 0 because there's no path to consider.

We calculate the maximum path sum for the left and right subtrees of the current node. If the calculated sum is negative, we set it to 0, as it's better not to include a negative sum in the path.

We update the self.max_sum variable by considering the path through the current node, which is the sum of the left and right subtree sums plus the value of the current node.

Finally, we return the maximum path sum starting from the current node, which is the maximum of the sums of the left and right subtrees plus the current node's value.

We start the recursion by calling maxPathSumFromNode(root) from the root node.

After the recursion, we return self.max_sum, which contains the maximum path sum overall.

You can use this maxPathSum function to find the maximum path sum in a binary tree, as demonstrated in the examples you provided
"""