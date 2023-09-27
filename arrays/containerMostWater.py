"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104

"""
def maxArea(height):
    max_water = 0  # Initialize the maximum water volume to 0
    left, right = 0, len(height) - 1  # Initialize two pointers, one at the start and one at the end
    
    while left < right:
        # Calculate the width between the two pointers (indices)
        width = right - left
        
        # Determine the minimum height between the two vertical lines
        min_height = min(height[left], height[right])
        
        # Calculate the water volume using the width and minimum height
        water = width * min_height
        
        # Update the maximum water volume if the current water volume is greater
        max_water = max(max_water, water)
        
        # Move the pointer with the smaller height towards the other pointer
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_water