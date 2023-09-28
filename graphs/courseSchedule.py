"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
"""


def canFinish(numCourses, prerequisites):
    # Create an adjacency list to represent the graph
    graph = [[] for _ in range(numCourses)]
    
    # Create an array to track the visited status of each course
    visited = [0] * numCourses
    
    # Build the graph
    for course, prereq in prerequisites:
        graph[course].append(prereq)
    
    # Define a DFS function
    def dfs(course):
        # If we encounter a visited node with status 1, it's a cycle
        if visited[course] == 1:
            return False
        
        # If we encounter a visited node with status 2, it's safe
        if visited[course] == 2:
            return True
        
        # Mark the course as being visited (status 1)
        visited[course] = 1
        
        # Recursively visit all prerequisites
        for prereq in graph[course]:
            if not dfs(prereq):
                return False
        
        # Mark the course as visited and safe (status 2)
        visited[course] = 2
        return True
    
    # Perform DFS for each course
    for course in range(numCourses):
        if not dfs(course):
            return False
    
    return True

"""
We create an adjacency list graph to represent the graph, and an array visited to keep track of the visited status of each course. The values of visited can be 0 (not visited), 1 (visited and in progress), or 2 (visited and safe).

We build the graph based on the prerequisites.

We define a DFS function dfs that checks for cycles in the graph. If it encounters a course that is currently being visited (status 1), it means there is a cycle, and we return False. If it encounters a course that is already visited and safe (status 2), we return True. Otherwise, we mark the course as being visited (status 1), recursively visit its prerequisites, and mark the course as visited and safe (status 2) if no cycle is found.

We perform the DFS for each course to check if it's possible to finish all courses.

Runtime Complexity: The time complexity of this solution is O(V + E), where V is the number of courses (nodes) and E is the number of prerequisites (edges). The space complexity is O(V + E) as well due to the space used for the adjacency list and the visited array.

This DFS approach provides a concise solution for the problem.

Sure, let's walk through the code step by step using an example:

Example:

lua
Copy code
numCourses = 4
prerequisites = [[1,0],[2,1],[3,2]]
Initialize graph and visited:

css
Copy code
graph = [[], [0], [1], [2]]
visited = [0, 0, 0, 0]
Build the graph based on prerequisites:

css
Copy code
graph[1] = [0]
graph[2] = [1]
graph[3] = [2]
Start DFS for each course:

DFS for Course 0 (visited[0] = 0):
Mark course 0 as being visited (visited[0] = 1).
Recursively visit its prerequisites (course 1).
DFS for Course 1 (visited[1] = 0):
Mark course 1 as being visited (visited[1] = 1).
Recursively visit its prerequisites (course 0).
However, course 0 is already being visited (visited[0] = 1), indicating a cycle.
Return False for course 1.
Since course 1 returned False, we return False for course 0.
The result is False because there is a cycle in the graph, meaning it's not possible to finish all courses.

Explanation:
The DFS algorithm explores the graph while keeping track of the visited status of each course. It detects cycles by checking if a course is being visited while already in progress. If a cycle is detected at any point during the DFS, the function returns False. Otherwise, it returns True if the DFS completes successfully for all courses.

In this example, the presence of the cycle [1, 0] makes it impossible to finish all courses, so the function correctly returns False.
"""