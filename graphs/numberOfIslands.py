"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""

def numIslands(grid):
    if not grid:
        return 0  # Return 0 if the grid is empty

    m, n = len(grid), len(grid[0])
    count = 0  # Initialize island count

    # Depth-first search function to explore islands
    def dfs(r, c):
        if 0 <= r < m and 0 <= c < n and grid[r][c] == '1':
            grid[r][c] = '0'  # Mark the current land as visited
            # Explore adjacent lands in all four directions
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

    # Loop through the grid to find islands
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                count += 1  # Found an unvisited land, increment island count
                dfs(i, j)  # Explore the island using DFS

    return count  # Return the total number of islands


"""
We first handle the base case by checking if the grid is empty. If it's empty, we return 0 because there are no islands.

We get the dimensions of the grid (m rows and n columns) and initialize the island count to 0.

We define a depth-first search (DFS) function called dfs that explores islands by checking neighboring cells. It marks visited land cells as '0' to avoid counting them multiple times.

We iterate through the grid using nested loops to find land cells ('1'). When we find an unvisited land cell, we increment the island count and explore the entire island using the dfs function.

After looping through the entire grid, we return the island count, which represents the total number of islands.

Runtime Complexity: The time complexity of this solution is O(m * n), where m is the number of rows and n is the number of columns in the grid. We visit each cell at most once.

Input Grid:

css
Copy code
[  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
We start at the top-left corner, find land ('1'), increment the island count to 1, and explore the entire island using DFS, marking visited cells as '0'.

We move to the next land cell ('1') and repeat the process. However, this time, we don't increment the island count because it's part of the same island as before.

We continue this process for the remaining land cells.

The final island count is 1 because there is one connected island in this grid.

"""