"""
You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.

Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2

Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1


Constraints:

1 <= n <= 2000
1 <= edges.length <= 5000
edges[i].length == 2
0 <= ai <= bi < n
ai != bi
There are no repeated edges.

"""

def countComponents(n, edges):
    # Create an adjacency list to represent the graph.
    adjacency_list = [[] for _ in range(n)]  
    for u, v in edges:
        adjacency_list[u].append(v)  # Add v as a neighbor of u
        adjacency_list[v].append(u)  # Add u as a neighbor of v (undirected edge).

    def dfs(node):
        # Mark the node as visited.
        visited[node] = True
        for neighbor in adjacency_list[node]:
            if not visited[neighbor]:
                dfs(neighbor)  # Recursively visit all connected neighbors.

    visited = [False] * n  # To keep track of visited nodes.
    connected_components = 0  # Initialize the count of connected components.

    for i in range(n):
        if not visited[i]:
            # Start a new DFS traversal from an unvisited node.
            dfs(i)
            connected_components += 1  # Increment the count for each connected component.

    return connected_components  # Return the total count of connected components.

# Example 1:
n1 = 5
edges1 = [[0, 1], [1, 2], [3, 4]]
print(countComponents(n1, edges1))  # Output: 2

# Example 2:
n2 = 5
edges2 = [[0, 1], [1, 2], [2, 3], [3, 4]]
print(countComponents(n2, edges2))  # Output: 1

"""
We create an adjacency list (adjacency_list) to represent the graph. Each node's adjacency list contains its neighboring nodes.

We iterate through the input edges and add each edge's vertices to the adjacency list. For undirected edges, we add both directions (i.e., both u and v as neighbors of each other).

We define a recursive DFS function called dfs. It starts from a node and explores all connected nodes while marking them as visited.

We initialize a list visited to keep track of visited nodes and a variable connected_components to count the number of connected components.

We iterate through all nodes (from 0 to n-1) and start a new DFS traversal if the node hasn't been visited yet. Each DFS traversal will cover one connected component.

After all DFS traversals are complete, connected_components holds the count of connected components in the graph.

Finally, we return the total count of connected components as the result.

This code efficiently finds and counts the connected components in the graph based on the given inputs.

Example 1:

Input:

python
Copy code
n1 = 5
edges1 = [[0, 1], [1, 2], [3, 4]]
Step 1: Create an adjacency list to represent the graph. Initialize an empty list for each node.

python
Copy code
adjacency_list = [[], [], [], [], []]
Iterate through the edges and add the vertices to the adjacency list:

Edge [0, 1]: Add 1 as a neighbor of 0 and 0 as a neighbor of 1 (undirected edge).
Edge [1, 2]: Add 2 as a neighbor of 1 and 1 as a neighbor of 2.
Edge [3, 4]: Add 4 as a neighbor of 3 and 3 as a neighbor of 4.
Now, adjacency_list looks like this:

python
Copy code
adjacency_list = [[1], [0, 2], [1], [4], [3]]
Step 2: Define a recursive DFS function called dfs.

Step 3: Initialize a list visited to keep track of visited nodes and a variable connected_components to count the number of connected components.

python
Copy code
visited = [False, False, False, False, False]
connected_components = 0
Step 4: Iterate through all nodes (from 0 to n-1) and start a new DFS traversal if the node hasn't been visited yet.

Start DFS from node 0:

Mark 0 as visited: visited = [True, False, False, False, False]
Explore its neighbor 1:
Mark 1 as visited: visited = [True, True, False, False, False]
Explore its neighbor 2:
Mark 2 as visited: visited = [True, True, True, False, False]
There are no more unvisited neighbors of 2.
There are no more unvisited neighbors of 1.
Start DFS from node 3:

Mark 3 as visited: visited = [True, True, True, True, False]
Explore its neighbor 4:
Mark 4 as visited: visited = [True, True, True, True, True]
There are no more unvisited neighbors of 3.
Step 5: After all DFS traversals are complete, connected_components holds the count of connected components. In this case, there are two connected components.

Step 6: Return the total count of connected components as the result. In this case, the result is 2.

Example 2:

Input:

python
Copy code
n2 = 5
edges2 = [[0, 1], [1, 2], [2, 3], [3, 4]]
Step 1: Create an adjacency list and initialize it as follows:

python
Copy code
adjacency_list = [[1], [0, 2], [1, 3], [2, 4], [3]]
Step 2 to Step 6: Follow the same steps as in Example 1 to perform DFS traversal and count connected components.

Start DFS from node 0. It will visit nodes 0, 1, 2, 3, and 4 as they are all connected. One connected component is found.

The final count of connected components is 1.

For Example 2, the code correctly identifies that there is only one connected component in the graph.

The code efficiently counts the number of connected components in the given graph using Depth-First Search (DFS).

"""
