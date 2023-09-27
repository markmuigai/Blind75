"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""
def productExceptSelf(nums):
    n = len(nums)
    
    # Initialize two arrays to store prefix and suffix products
    prefix_product = [1] * n  # Initialize a prefix product array with all 1s.
    suffix_product = [1] * n  # Initialize a suffix product array with all 1s.
    
    # Calculate prefix products
    prefix = 1  # Initialize a variable to keep track of the prefix product.
    for i in range(n):
        prefix_product[i] = prefix  # Store the current prefix product in the array.
        prefix *= nums[i]  # Update the prefix product by multiplying with the current element.
    
    # Calculate suffix products
    suffix = 1  # Initialize a variable to keep track of the suffix product.
    # n - 1: This is the starting value of i.
    # -1: This is the ending value of i. The loop will continue until i is greater than or equal to -1.
    # -1: This is the step value. It determines how i is incremented or decremented after each iteration.
    for i in range(n - 1, -1, -1):
        suffix_product[i] = suffix  # Store the current suffix product in the array.
        suffix *= nums[i]  # Update the suffix product by multiplying with the current element.
    
    # Calculate the final answer using prefix and suffix products
    answer = [prefix_product[i] * suffix_product[i] for i in range(n)]
    
    return answer

# Example 1
nums1 = [1, 2, 3, 4]
print(productExceptSelf(nums1))  # Output: [24, 12, 8, 6]

# Example 2
nums2 = [-1, 1, 0, -3, 3]
print(productExceptSelf(nums2))  # Output: [0, 0, 9, 0, 0]
