"""

"""

from queue import Queue  # Import the Queue class

class TreeNode:
    def __init__(self, value=0, left_child=None, right_child=None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

def levelOrderTraversal(root):
    # Create a queue to perform BFS
    queue = Queue()

    # Start by adding the root node to the queue
    queue.put(root)

    # Initialize an empty list to store the BFS traversal order
    bfs_order = []

    # Perform BFS traversal
    while not queue.empty():
        # Get the current node from the front of the queue
        current_node = queue.get()

        # Append the value of the current node to the BFS order list
        bfs_order.append(current_node.value)

        # Add the left child to the queue if it exists
        if current_node.left_child:
            queue.put(current_node.left_child)

        # Add the right child to the queue if it exists
        if current_node.right_child:
            queue.put(current_node.right_child)

    # Return the BFS traversal order as a list
    return bfs_order

"""
Import the Queue class from the queue module.

Define the TreeNode class to represent nodes in the binary tree. It includes a value, a left child, and a right child.

Define the levelOrderTraversal function, which takes the root of the binary tree as input.

Create a Queue object named queue to perform the breadth-first search (BFS) traversal.

Start the BFS traversal by adding the root node to the queue using queue.put(root).

Initialize an empty list bfs_order to store the BFS traversal order.

Perform the BFS traversal in a loop until the queue is empty:

Get the current node from the front of the queue using current_node = queue.get().

Append the value of the current node to the bfs_order list using bfs_order.append(current_node.value).

If the current node has a left child, add it to the queue using queue.put(current_node.left_child).

If the current node has a right child, add it to the queue using queue.put(current_node.right_child).

After completing the BFS traversal, return the bfs_order list, which contains the values of nodes in level order.

You can use this levelOrderTraversal function to obtain the level order traversal of a binary tree by passing the root of the tree as an argument.
"""