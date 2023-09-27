"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
 

Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
"""

def coinChange(coins, amount):
    # Create an array 'dp' to store the minimum number of coins needed to make up each amount.
    # Initialize it with a value greater than the maximum possible number of coins required.
    dp = [float('inf')] * (amount + 1)
    
    # The number of coins needed to make up amount 0 is 0.
    dp[0] = 0
    
    # Iterate through each coin denomination.
    for coin in coins:
        # For each coin denomination, iterate through amounts from the coin value to the target amount.
        for i in range(coin, amount + 1):
            # Update 'dp[i]' with the minimum of its current value and 'dp[i - coin] + 1',
            # which represents using one coin of denomination 'coin'.
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # If 'dp[amount]' remains greater than the initial value, it means it's impossible
    # to make up the amount with the given coins, so return -1.
    if dp[amount] == float('inf'):
        return -1
    else:
        return dp[amount]

# Example usage:
coins = [1, 2, 5]
amount = 11
result = coinChange(coins, amount)
print("Fewest number of coins needed:", result)

"""
We define a function coinChange that takes two arguments: coins, representing the coin denominations, and amount, representing the target amount.

We create an array dp of length (amount + 1) to store the minimum number of coins needed to make up each amount. We initialize all elements with a value of float('inf') to represent initially unknown values.

We set dp[0] to 0 because the minimum number of coins needed to make up amount 0 is 0.

We iterate through each coin denomination in the coins list.

For each coin denomination, we iterate through amounts from the coin value to the target amount.

Inside the nested loop, we update dp[i] with the minimum of its current value and dp[i - coin] + 1, which represents using one coin of denomination coin.

The nested loops continue until we've calculated the minimum number of coins needed for all amounts up to the target amount.

After the loops, if dp[amount] remains greater than the initial value (float('inf')), it means it's impossible to make up the amount with the given coins, so we return -1.

If dp[amount] has a value less than float('inf'), we return that value, which represents the fewest number of coins needed to make up the target amount.

In the example with coins = [1,2,5] and amount = 11, the code will calculate the fewest number of coins needed, which is 3 (11 = 5 + 5 + 1), and print that result.
"""