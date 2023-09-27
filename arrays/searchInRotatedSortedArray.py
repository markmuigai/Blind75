"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
 

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104
"""

def search(nums, target):
    # Initialize two pointers, left and right, to define the search range
    left, right = 0, len(nums) - 1
    
    while left <= right:
        # Calculate the middle index of the current search range
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            return mid  # Target found, return its index
        
        # If the left half of the array is sorted (no rotation)
        if nums[left] <= nums[mid]:
            # Target is in the left half, update right pointer
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                # Target is in the right half, update left pointer
                left = mid + 1
        else:
            # If the right half of the array is sorted (rotation present)
            if nums[mid] < target <= nums[right]:
                # Target is in the right half, update left pointer
                left = mid + 1
            else:
                # Target is in the left half, update right pointer
                right = mid - 1
    
    return -1  # Target not found

# Example 1
nums1 = [4, 5, 6, 7, 0, 1, 2]
target1 = 0
# Initial range: [0, 6]
# 1st iteration: mid = 3, nums[3] = 7, nums[left] <= nums[mid], left = mid + 1
# 2nd iteration: mid = 5, nums[5] = 1, nums[left] > nums[mid], right = mid - 1
# 3rd iteration: mid = 4, nums[4] = 0, nums[mid] == target, return 4 (index of target)
print(search(nums1, target1))  # Output: 4

# Example 2
nums2 = [4, 5, 6, 7, 0, 1, 2]
target2 = 3
# Initial range: [0, 6]
# 1st iteration: mid = 3, nums[3] = 7, nums[left] <= nums[mid], left = mid + 1
# 2nd iteration: mid = 5, nums[5] = 1, nums[left] > nums[mid], right = mid - 1
# 3rd iteration: mid = 4, nums[4] = 0, nums[mid] != target, continue searching
# Left pointer crosses right pointer, target not found, return -1
print(search(nums2, target2))  # Output: -1

# Example 3
nums3 = [1]
target3 = 0
# Initial range: [0, 0]
# 1st iteration: mid = 0, nums[0] = 1, nums[mid] != target, target not found, return -1
print(search(nums3, target3))  # Output: -1
