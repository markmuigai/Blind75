"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
 

Constraints:

n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
All the integers of nums are unique.
nums is sorted and rotated between 1 and n times.
"""

def findMin(nums):
    # Initialize two pointers, left and right, to define the search range
    left, right = 0, len(nums) - 1
    
    # Perform a binary search until the left pointer is less than the right pointer
    while left < right:
        # Calculate the middle index of the search range
        mid = left + (right - left) // 2
        
        # If the middle element is greater than the rightmost element,
        # it means the minimum element is on the right side of the middle
        if nums[mid] > nums[right]:
            left = mid + 1
        # If the middle element is less than or equal to the rightmost element,
        # it means the minimum element is on the left side of the middle
        else:
            right = mid
    
    # The left pointer now points to the minimum element
    return nums[left]

# Example 1
nums1 = [3, 4, 5, 1, 2]
# Initial range: [0, 4]
# 1st iteration: mid = 2, nums[2] > nums[4], so update left to 3
# 2nd iteration: mid = 3, nums[3] < nums[4], so update right to 3
# Now left = right = 3, pointing to the minimum element (1)
print(findMin(nums1))  # Output: 1

# Example 2
nums2 = [4, 5, 6, 7, 0, 1, 2]
# Initial range: [0, 6]
# 1st iteration: mid = 3, nums[3] < nums[6], so update right to 3
# Now left = right = 3, pointing to the minimum element (0)
print(findMin(nums2))  # Output: 0

# Example 3
nums3 = [11, 13, 15, 17]
# Initial range: [0, 3]
# 1st iteration: mid = 1, nums[1] < nums[3], so update right to 1
# Now left = right = 1, pointing to the minimum element (13)
print(findMin(nums3))  # Output: 11
