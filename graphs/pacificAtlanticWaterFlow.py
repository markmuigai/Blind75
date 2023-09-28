"""
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans. Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean 
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean 
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean 
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean 
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean 
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
Example 2:

Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.
"""

def pacificAtlantic(heights):
    if not heights:
        return []  # Return an empty list if the input grid is empty

    m, n = len(heights), len(heights[0])  # Get the dimensions of the grid
    pacific_reachable = [[False] * n for _ in range(m)]  # Initialize matrix for cells that can reach Pacific
    atlantic_reachable = [[False] * n for _ in range(m)]  # Initialize matrix for cells that can reach Atlantic
    result = []  # Initialize the result list to store coordinates

    # Depth-first search function to explore reachable cells
    def dfs(r, c, reachable):
        reachable[r][c] = True  # Mark the current cell as reachable
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc  # Calculate neighboring cell coordinates
            if 0 <= nr < m and 0 <= nc < n and not reachable[nr][nc] and heights[nr][nc] >= heights[r][c]:
                # Check if the neighbor is within bounds, not reached before, and can flow to
                dfs(nr, nc, reachable)  # Recursively explore the neighbor

    # Start DFS from cells on the borders
    for i in range(m):
        dfs(i, 0, pacific_reachable)  # Start DFS from the left border to reach the Pacific
        dfs(i, n - 1, atlantic_reachable)  # Start DFS from the right border to reach the Atlantic
    for j in range(n):
        dfs(0, j, pacific_reachable)  # Start DFS from the top border to reach the Pacific
        dfs(m - 1, j, atlantic_reachable)  # Start DFS from the bottom border to reach the Atlantic

    # Find the cells that can reach both oceans
    for i in range(m):
        for j in range(n):
            if pacific_reachable[i][j] and atlantic_reachable[i][j]:
                result.append([i, j])  # Add coordinates to the result list if reachable by both oceans

    return result  # Return the list of coordinates where rainwater can flow to both oceans

"""
Example Grid:

css
Copy code
heights = [[1, 2, 2, 3, 5],
           [3, 2, 3, 4, 4],
           [2, 4, 5, 3, 1],
           [6, 7, 1, 4, 5],
           [5, 1, 1, 2, 4]]
Step 1: Initialize two grids, pacific_reachable and atlantic_reachable, of the same size as the input grid. These grids will help us track which cells can reach the Pacific Ocean and the Atlantic Ocean.

Step 2: Define a Depth-First Search (DFS) function (dfs) that explores cells by checking their elevation compared to neighboring cells. If a cell's elevation is higher than its neighbor, it's not reachable. Otherwise, it's reachable.

Step 3: Start DFS from cells along the borders of the grid. We check which cells can reach the Pacific Ocean and the Atlantic Ocean. Let's start with the left and right borders:

Left Border (Pacific Ocean):

We explore cells along the left border and mark them as "reachable" in the pacific_reachable grid if they can flow to the Pacific Ocean.
For example, cell [0, 0] can reach the Pacific Ocean, so we mark it as reachable.
Cell [1, 0] can also reach the Pacific Ocean through [0, 0], so we mark it as reachable.
Right Border (Atlantic Ocean):

We explore cells along the right border and mark them as "reachable" in the atlantic_reachable grid if they can flow to the Atlantic Ocean.
For example, cell [0, 4] can reach the Atlantic Ocean, so we mark it as reachable.
Cell [1, 4] can also reach the Atlantic Ocean through [0, 4], so we mark it as reachable.
We perform similar steps for the top and bottom borders.

Step 4: During DFS traversal, we mark cells as "reachable" in the pacific_reachable and atlantic_reachable grids when we find a path from a border cell to that cell.

Step 5: After DFS, we compare both pacific_reachable and atlantic_reachable grids to find cells that can reach both oceans. If a cell is marked as "reachable" in both grids, it means rainwater can flow from that cell to both the Pacific and Atlantic Oceans.

Step 6: We collect the coordinates of these cells and return them as the result. In our example, the following cells meet this condition:

[0, 4]
[1, 3]
[1, 4]
[2, 2]
[3, 0]
[3, 1]
[4, 0]
These cells can flow to both the Pacific and Atlantic Oceans, as rainwater can follow paths through the elevation differences in the grid.
"""