"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""
def climbStairs(n):
    # Create an array to store the number of ways to reach each step.
    # Initialize it with zeros, and set the base cases.
    dp = [0] * (n + 1)
    dp[0] = 1  # There is one way to reach step 0 (no steps).
    dp[1] = 1  # There is one way to reach step 1 (take one step).

    # Iterate through the steps from 2 to n and calculate the number of ways
    # to reach each step based on the previous steps.
    for i in range(2, n + 1):
        # The number of ways to reach step i is the sum of the ways to reach
        # step (i-1) and step (i-2) because you can either take 1 or 2 steps at a time.
        dp[i] = dp[i - 1] + dp[i - 2]

    # The final result is stored in dp[n], which represents the number of ways
    # to reach the top step (n).
    return dp[n]

# Example usage:
n = 3
result = climbStairs(n)
print("Number of distinct ways to climb to the top:", result)

"""
Here's the step-by-step execution for n = 5:

We create an array dp with a length of 6 (from index 0 to 5) to store the number of ways to reach each step. All elements are initialized to 0.

We set the base cases:

dp[0] = 1: There is one way to reach step 0 (no steps).
dp[1] = 1: There is one way to reach step 1 (take one step).
We enter a for loop to iterate through the steps from 2 to 5.

In the first iteration (i = 2), we calculate dp[2] as dp[1] + dp[0], which is 1 + 1 = 2. This means there are two ways to reach step 2.

In the second iteration (i = 3), we calculate dp[3] as dp[2] + dp[1], which is 2 + 1 = 3. So, there are three ways to reach step 3.

We continue this process for steps 4 and 5.

Finally, we return dp[5], which is the result. dp[5] represents the number of distinct ways to climb to the top when there are 5 steps, and the result is 8.

So, for n = 5, there are 8 distinct ways to climb to the top of the staircase.


"""