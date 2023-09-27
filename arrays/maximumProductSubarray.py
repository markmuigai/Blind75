"""
Given an integer array nums, find a 
subarray
that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.


Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""

def maxProduct(nums):
    if not nums:
        return 0
    
    # Initialize variables to keep track of the maximum and minimum products ending at each position
    max_product = nums[0]  # Maximum product ending at the current position
    min_product = nums[0]  # Minimum product ending at the current position
    result = nums[0]      # Overall maximum product
    
    # Iterate through the array starting from the second element
    for i in range(1, len(nums)):
        # If the current number is negative, swapping max_product and min_product is important
        if nums[i] < 0:
            max_product, min_product = min_product, max_product
            # When we encounter a negative number, swapping the maximum and minimum products is essential
            # because multiplying a negative number can turn the maximum into the minimum, and vice versa.
        
        # Update max_product and min_product for the current position
        # The maximum product can either be the current number itself or the product of the previous maximum
        # and the current number. Similarly, the minimum product can be the current number or the product
        # of the previous minimum and the current number.
        max_product = max(nums[i], max_product * nums[i])
        min_product = min(nums[i], min_product * nums[i])
        
        # Update the result with the maximum product found so far
        # At each step, we update the result with the maximum product seen so far, which ensures that
        # we capture the maximum product subarray.
        result = max(result, max_product)
    
    return result

# Example 1
nums1 = [2, 3, -2, 4]
# Initially, max_product = min_product = result = 2
# i = 1: max_product = 6, min_product = 3, result = 6
# i = 2: max_product = 3, min_product = -12, result = 6
# i = 3: max_product = 12, min_product = -24, result = 12
# The maximum product subarray is [2, 3] with a product of 6.
print(maxProduct(nums1))  # Output: 6

# Example 2
nums2 = [-2, 0, -1]
# Initially, max_product = min_product = result = -2
# i = 1: max_product = 0, min_product = 0, result = 0
# i = 2: max_product = 0, min_product = 0, result = 0
# The maximum product subarray is an empty subarray, and the maximum product is 0.
print(maxProduct(nums2))  # Output: 0
