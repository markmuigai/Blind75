"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
"""

def maxProfit(prices):
    # Initialize two pointers, one for buying and one for selling
    buy = 0
    sell = 0
    
    # Initialize the maximum profit to 0
    max_profit = 0
    
    # Iterate through the prices array
    while sell < len(prices):
        # If the price at the sell pointer is greater than the price at the buy pointer
        if prices[sell] > prices[buy]:
            # Calculate the current profit
            current_profit = prices[sell] - prices[buy]
            
            # Update the maximum profit if the current profit is greater
            max_profit = max(max_profit, current_profit)
            
        else:
            # If the price at sell is less than or equal to buy, update the buy pointer
            buy = sell
        
        # Move the sell pointer to the next day
        sell += 1
    
    return max_profit

# Example 1
prices1 = [7,1,5,3,6,4]
print(maxProfit(prices1))  # Output: 5

# Example 2
prices2 = [7,6,4,3,1]
print(maxProfit(prices2))  # Output: 0
