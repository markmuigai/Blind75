"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

def containsDuplicate(nums):
    # Create an empty set to store unique values
    unique_set = set()
    
    # Iterate through the array
    for num in nums:
        # If the current number is already in the set, it's a duplicate, so return True
        if num in unique_set:
            return True
        # Otherwise, add the number to the set
        else:
            unique_set.add(num)
    
    # If the loop completes without finding any duplicates, return False
    return False

# Example 1
nums1 = [1,2,3,1]
print(containsDuplicate(nums1))  # Output: True

# Example 2
nums2 = [1,2,3,4]
print(containsDuplicate(nums2))  # Output: False

# Example 3
nums3 = [1,1,1,3,3,4,3,2,4,2]
print(containsDuplicate(nums3))  # Output: True
