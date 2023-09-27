"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""

def threeSum(nums):
    # Sort the array in ascending order
    nums.sort()
    
    triplets = []  # Initialize an empty list to store triplets
    
    # Iterate through the array with a fixed first element (i)
    for i in range(len(nums) - 2):
        # Skip duplicates to avoid duplicate triplets
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        # Define two pointers, left and right, for the remaining elements
        left, right = i + 1, len(nums) - 1
        
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if total == 0:
                # Found a triplet with zero sum
                triplets.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates of left and right pointers
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1  # Move the left pointer to explore more solutions
                right -= 1  # Move the right pointer to explore more solutions
            elif total < 0:
                left += 1  # Increase the left pointer to make the sum closer to zero
            else:
                right -= 1  # Decrease the right pointer to make the sum closer to zero
    
    return triplets  # Return the list of unique triplets

# Example 1
nums1 = [-1, 0, 1, 2, -1, -4]
# After sorting: [-4, -1, -1, 0, 1, 2]
# Fixed element (i): -4
# Two pointers (left and right) find pairs that sum up to 4
# [-4, -1, 5] does not sum to 0, move left pointer
# [-4, -1, 5] does not sum to 0, move left pointer
# [-4, -1, 0] sums to 0, add to triplets
# Skip duplicates of left and right pointers
# [-4, -1, 0] sums to 0, add to triplets
# [-4, 0, 1] sums to 0, add to triplets
# [-4, 2, 2] does not sum to 0, move right pointer
# [-4, 2, 1] sums to 0, add to triplets
# Move i pointer to the next unique value (-1)
# [-1, -1, 2] sums to 0, add to triplets
# [-1, 0, 1] sums to 0, add to triplets
# Result: [[-1, -1, 2], [-1, 0, 1]]
print(threeSum(nums1))

# Example 2
nums2 = [0, 1, 1]
# After sorting: [0, 1, 1]
# No triplets sum to 0, result is an empty list
print(threeSum(nums2))

# Example 3
nums3 = [0, 0, 0]
# After sorting: [0, 0, 0]
# All elements are zeros, the only possible triplet is [0, 0, 0]
print(threeSum(nums3))

