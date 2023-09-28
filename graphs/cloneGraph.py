"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.


"""

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node):
    if not node:
        return None
    
    # Create a dictionary to map original nodes to their clones
    node_map = {}
    
    # Define a DFS function to traverse and clone the graph
    def dfs(original):
        # If the original node is not in the map, create a clone
        if original not in node_map:
            node_map[original] = Node(original.val)
            
            # Recursively clone its neighbors
            for neighbor in original.neighbors:
                node_map[original].neighbors.append(dfs(neighbor))
        
        return node_map[original]
    
    # Start the DFS from the given node (val=1)
    return dfs(node)

"""
We create a dictionary node_map to keep track of the mapping between original nodes and their clones.

We define a depth-first search (DFS) function called dfs that takes an original node as input. Inside this function, we check if the node has already been cloned. If not, we create a new clone node with the same value and add it to the node_map.

We then recursively clone the neighbors of the original node and add them to the neighbors list of the clone node.

Finally, we start the DFS from the given node (which is always the first node with val=1) and return the clone of that node.

Runtime Complexity: The time complexity of this solution is O(V + E), where V is the number of nodes (vertices) and E is the number of edges in the graph. This is because we visit each node and each edge exactly once during the DFS traversal.

Space Complexity: The space complexity is also O(V + E) because of the space used for the node_map dictionary and the recursive function call stack during the DFS traversal.
"""