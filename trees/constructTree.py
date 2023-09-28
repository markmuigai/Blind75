"""
Given two integer arrays preorder and inorder where preorder is the preorder traversal
of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

Example 1:


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]
 


"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder, inorder):
    # Base case: If either list is empty, return None
    if not preorder or not inorder:
        return None

    # Get the root value from the preorder list (it's the first element)
    root_val = preorder[0]

    # Create a TreeNode for the root with the root value
    root = TreeNode(root_val)

    # Find the index of the root value in the inorder list
    root_index = inorder.index(root_val)

    # Recursively build the left and right subtrees
    root.left = buildTree(preorder[1:1 + root_index], inorder[:root_index])
    root.right = buildTree(preorder[1 + root_index:], inorder[root_index + 1:])

    return root

"""
Step 1: Create TreeNode Class

We start by defining a class called TreeNode, which represents nodes in the binary tree. Each node has a value (val) and can have a left and right child.

Step 2: Initialize Pointers

We have two lists: the preorder traversal [3, 9, 20, 15, 7] and the inorder traversal [9, 3, 15, 20, 7]. We'll also initialize some pointers and variables to keep track of our progress.

preorder points to the current position in the preorder traversal.
inorder points to the current position in the inorder traversal.
Step 3: Build the Root Node

We start by looking at the first element of the preorder traversal, which is 3. This is the root of the binary tree.

We create a TreeNode with a value of 3 and assign it as the root node.

Next, we find the index of 3 in the inorder traversal, which is at index 1. This tells us that the elements to the left of index 1 in the inorder traversal are the left subtree of the root, and the elements to the right are the right subtree.

We recursively build the left and right subtrees of the root node.

Step 4: Build the Left Subtree

For the left subtree, we focus on the elements [9] in the preorder traversal and [9] in the inorder traversal.

We take the first element from the preorder traversal, which is 9, and create a TreeNode with a value of 9. This becomes the left child of the root node.

There are no elements to the left or right of 9 in the inorder traversal, so the left subtree is complete.

Step 5: Build the Right Subtree

For the right subtree, we focus on the elements [20, 15, 7] in the preorder traversal and [15, 20, 7] in the inorder traversal.

We take the first element from the preorder traversal, which is 20, and create a TreeNode with a value of 20. This becomes the right child of the root node.

We find the index of 20 in the inorder traversal, which is at index 1. This indicates that 15 and 7 are elements in the right subtree.

We recursively build the left and right subtrees for the 20 node.

For the left subtree of 20, we focus on the elements [15] in the preorder traversal and [15] in the inorder traversal. We create a TreeNode with a value of 15, and there are no further elements to consider.

For the right subtree of 20, we focus on the elements [7] in the preorder traversal and [7] in the inorder traversal. We create a TreeNode with a value of 7, and there are no further elements to consider.

Step 6: Completion

The entire binary tree has been constructed.

The root node is 3, with a left child of 9 and a right child of 20.

The 20 node has a left child of 15 and a right child of 7.
"""