"""
Given an integer array nums, find the 
subarray
 with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
"""
def maxSubArray(nums):
    # Initialize variables to keep track of the current maximum sum and the maximum sum overall
    current_max = nums[0]
    max_sum = nums[0]
    
    # Iterate through the array starting from the second element
    for i in range(1, len(nums)):
        # Calculate the current maximum sum by choosing the maximum between the current element
        # and the current element combined with the previous maximum sum
        current_max = max(nums[i], current_max + nums[i])
        
        # Update the maximum sum if the current maximum sum is greater
        max_sum = max(max_sum, current_max)
    
    return max_sum

# Example 1
nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(nums1))  # Output: 6

# Example 2
nums2 = [1]
print(maxSubArray(nums2))  # Output: 1

# Example 3
nums3 = [5, 4, -1, 7, 8]
print(maxSubArray(nums3))  # Output: 23
