"""
Given an integer array nums, return the length of the longest strictly increasing 
subsequence
.

 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
 

Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104
 

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
"""

def lengthOfLIS(nums):
    # Initialize a list called 'tails' to store the smallest tail of increasing subsequences.
    # 'tails' is a dynamic array where 'tails[i]' represents the smallest tail of increasing subsequence of length 'i+1'.
    tails = [0] * len(nums)
    
    # Initialize a variable 'size' to keep track of the current size of the subsequences.
    size = 0
    
    for num in nums:
        # Binary search to find the index 'i' where 'num' can be inserted into 'tails' to maintain increasing order.
        left, right = 0, size
        while left < right:
            mid = (left + right) // 2  # Calculate the middle index.
            if tails[mid] < num:
                left = mid + 1  # Adjust 'left' to search the right half.
            else:
                right = mid  # Adjust 'right' to search the left half.
        
        # Update 'tails' at the index 'left' with 'num'.
        tails[left] = num
        
        # If 'num' is larger than any tail in 'tails', increment 'size'.
        if left == size:
            size += 1
    
    # 'size' represents the length of the longest increasing subsequence.
    return size

# Example usage:
nums1 = [10, 9, 2, 5, 3, 7, 101, 18]
result1 = lengthOfLIS(nums1)
print("Longest increasing subsequence length:", result1)

nums2 = [0, 1, 0, 3, 2, 3]
result2 = lengthOfLIS(nums2)
print("Longest increasing subsequence length:", result2)

nums3 = [7, 7, 7, 7, 7, 7, 7]
result3 = lengthOfLIS(nums3)
print("Longest increasing subsequence length:", result3)


"""
We define a function lengthOfLIS that takes a list nums as input.

We initialize an empty list called tails. This list will store the smallest tail of increasing subsequences.

In this context, "tails" refers to the last element of an increasing subsequence. Specifically, tails[i] represents the smallest value among the last elements of all increasing subsequences of length i+1. For example, if tails[2] is 5, it means that 5 is the smallest tail of all increasing subsequences of length 3.

We initialize a variable size to 0. This variable will keep track of the current size of the subsequences.

We start iterating through the elements in the nums list using a for loop.

For each element num in nums, we perform a binary search in the tails list to find the correct position for num to maintain increasing order.

We initialize two pointers, left and right, to perform the binary search. left starts at 0, and right starts at the current value of size.

Inside the while loop, we calculate the middle index mid as the average of left and right.

We compare tails[mid] with num to determine whether num should be placed to the left or right of mid.

If tails[mid] is less than num, we adjust the left pointer to mid + 1, indicating that we should search the right half of the subsequence.

If tails[mid] is greater than or equal to num, we adjust the right pointer to mid, indicating that we should search the left half of the subsequence.

We continue the binary search until left is no longer less than right.

After exiting the while loop, we update tails at the index left with the value of num. This effectively inserts num into the correct position in the tails list.

If left is equal to size, it means that num is larger than any tail in tails. In this case, we increment size to indicate that we have extended the length of the longest increasing subsequence.

We repeat the above process for all elements in nums.

After processing all elements, the value of size represents the length of the longest increasing subsequence.

Finally, we return the value of size, which is the length of the longest increasing subsequence.
"""

