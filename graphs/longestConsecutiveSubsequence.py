"""

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109"""

def longestConsecutive(nums):
    # Step 1: Convert the input list into a set for faster lookup
    num_set = set(nums)  
    max_length = 0  # Initialize the maximum consecutive sequence length

    # Step 2: Iterate through each unique number in the set
    for num in num_set:  
        # Step 3: Check if num is the potential start of a sequence
        if num - 1 not in num_set:  
            current_num = num  # Initialize current_num with the potential start
            current_length = 1  # Initialize the current sequence length

            # Step 4: Extend the sequence as long as possible
            while current_num + 1 in num_set:  
                current_num += 1
                current_length += 1

            # Step 5: Update the maximum sequence length
            max_length = max(max_length, current_length)  

    # Step 6: Return the length of the longest consecutive sequence
    return max_length  


"""
We start by converting the input list nums into a set called num_set. This conversion allows us to perform faster lookup operations because set membership checks are efficient.

We initialize a variable max_length to keep track of the maximum consecutive sequence length.

We iterate through each number in the num_set:

For each number, we check if num - 1 is not in num_set. If it's not present, it means that num can be the potential start of a consecutive sequence.

We initialize current_num with the current number and current_length as 1 to represent the sequence starting from num.

We use a while loop to extend the sequence as long as possible. We keep incrementing current_num by 1 and current_length by 1 as long as current_num + 1 is present in num_set.

We update max_length with the maximum value between its current value and current_length. This ensures that we keep track of the longest consecutive sequence encountered so far.

After the loop, max_length holds the length of the longest consecutive sequence in the array, and we return it as the result.

This code efficiently finds the length of the longest consecutive sequence in the input list nums while maintaining O(n) time complexity.

Example Input:

css
Copy code
nums = [100, 4, 200, 1, 3, 2]
Step 1: Convert the input list into a set for faster lookup.

makefile
Copy code
num_set = {100, 4, 200, 1, 3, 2}
Step 2: Initialize max_length to 0. This variable will store the maximum consecutive sequence length.

makefile
Copy code
max_length = 0
Step 3: Iterate through each unique number in the set num_set:

For num = 100, we check if 99 is not in num_set. It's not present, so we consider 100 as the potential start of a consecutive sequence.

Initialize current_num as 100.
Initialize current_length as 1.
Step 4: Extend the sequence as long as possible:

We enter a while loop and check if current_num + 1 (i.e., 101) is in num_set. If yes, we increment current_num and current_length.

Increment current_num to 101.
Increment current_length to 2.
We continue this process until we can't find current_num + 1 in num_set.

Step 5: Update the max_length with the maximum value between its current value and current_length. In this case, current_length is 2, and max_length is updated accordingly.

makefile
Copy code
max_length = max(0, 2)  # max_length is now 2
Step 6: Continue the loop for the next unique number in num_set.

For num = 4, we check if 3 is not in num_set. It's not present, so we consider 4 as the potential start of a consecutive sequence.

Initialize current_num as 4.
Initialize current_length as 1.
Extend the sequence as long as possible:

We increment current_num and current_length as long as current_num + 1 is in num_set.
Step 5: Update max_length again with the maximum value between its current value (2) and current_length. In this case, current_length is greater than max_length, so max_length is updated to current_length.

makefile
Copy code
max_length = max(2, 3)  # max_length is now 3
Step 6: Continue the loop for the next unique number in num_set.

For num = 200, we check if 199 is not in num_set. It's not present, so we consider 200 as the potential start of a consecutive sequence.

Initialize current_num as 200.
Initialize current_length as 1.
Extend the sequence as long as possible:

We increment current_num and current_length as long as current_num + 1 is in num_set.
Step 5: Update max_length with the maximum value between its current value (3) and current_length. In this case, current_length is not greater than max_length, so max_length remains 3.

Step 6: Continue the loop for the next unique number in num_set.

For num = 1, we check if 0 is not in num_set. It's not present, so we consider 1 as the potential start of a consecutive sequence.

Initialize current_num as 1.
Initialize current_length as 1.
Extend the sequence as long as possible:

We increment current_num and current_length as long as current_num + 1 is in num_set.
Step 5: Update max_length with the maximum value between its current value (3) and current_length. In this case, current_length is greater than max_length, so max_length is updated to current_length.

makefile
Copy code
max_length = max(3, 4)  # max_length is now 4
Step 6: Continue the loop for the next unique number in num_set.

For num = 3, we check if 2 is not in num_set. It's not present, so we consider 3 as the potential start of a consecutive sequence.

Initialize current_num as 3.
Initialize current_length as 1.
Extend the sequence as long as possible:

We increment current_num and current_length as long as current_num + 1 is in num_set.
Step 5: Update max_length with the maximum value between its current value (4) and current_length. In this case, current_length is not greater than max_length, so max_length remains 4.

Step 6: Continue the loop for the last unique number in num_set.

For num = 2, we check if 1 is not in num_set. It's not present, so we consider 2 as the potential start of a consecutive sequence.

Initialize current_num

"""