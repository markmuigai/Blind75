"""
Serialization is the process of converting a data structure or object into a sequence of
bits so that it can be stored in a file or memory buffer, or transmitted across a network connection
link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how
your serialization/deserialization algorithm should work. You just need to ensure that a binary
tree can be serialized to a string and this string can be deserialized to the original tree structure.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string."""
        # Helper function to perform preorder traversal and serialize the tree
        def preorder(node):
            if not node:
                result.append('None')
            else:
                result.append(str(node.val))
                preorder(node.left)
                preorder(node.right)
        
        result = []
        preorder(root)
        return ' '.join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        # Helper function to build the tree from the serialized data
        def build_tree():
            val = next(values)
            if val == 'None':
                return None
            node = TreeNode(int(val))
            node.left = build_tree()
            node.right = build_tree()
            return node
        
        values = iter(data.split())
        return build_tree()

# Create a simple binary tree for testing
#     1
#    / \
#   2   3
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

# Initialize the Codec
ser = Codec()
deser = Codec()

# Serialize the binary tree
serialized_tree = ser.serialize(root)
print("Serialized Tree:", serialized_tree)

# Deserialize the serialized data to reconstruct the tree
reconstructed_tree = deser.deserialize(serialized_tree)

# Verify that the reconstructed tree matches the original tree
print("Is the reconstructed tree the same as the original tree?")
print(root.val == reconstructed_tree.val)
print(root.left.val == reconstructed_tree.left.val)
print(root.right.val == reconstructed_tree.right.val)

"""
We define the TreeNode class to represent nodes in the binary tree.

We create a simple binary tree with three nodes (1, 2, and 3) for testing purposes.

We initialize the Codec class by creating two instances: ser for serialization and deser for deserialization.

We serialize the binary tree by calling ser.serialize(root) and store the result in serialized_tree.

We print the serialized tree to see the serialized representation.

We deserialize the serialized_tree using deser.deserialize(serialized_tree), which reconstructs the binary tree.

We verify that the reconstructed tree matches the original tree by comparing their values.

When you run this code, you should see that the reconstructed tree is the same as the original tree, demonstrating that the serialization and deserialization process works correctly.

The serialized tree representation is 1 2 None None 3 None None, where None represents null nodes.
"""