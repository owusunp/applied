"""
LeetCode #121 - Best Time to Buy and Sell Stock

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
- 1 <= prices.length <= 10^5
- 0 <= prices[i] <= 10^4

THOUGHT PROCESS FOR INTERVIEWER:

**Approach**: Track the minimum price seen so far and calculate max profit.

**How it works**:
- Keep track of the lowest price we've seen (best time to buy)
- For each price, calculate profit if we sell at that price
- Update maximum profit if current profit is better

**Key Points**:
- We need to buy before we sell (can't go backwards in time)
- Track minimum buy price as we go
- Calculate profit at each step: current price - minimum buy price
- Keep track of maximum profit seen

**Example**: prices = [7,1,5,3,6,4]
- Day 0: price=7, min_price=7, profit=0, max_profit=0
- Day 1: price=1, min_price=1, profit=0, max_profit=0
- Day 2: price=5, min_price=1, profit=5-1=4, max_profit=4
- Day 3: price=3, min_price=1, profit=3-1=2, max_profit=4
- Day 4: price=6, min_price=1, profit=6-1=5, max_profit=5
- Day 5: price=4, min_price=1, profit=4-1=3, max_profit=5

**Time Complexity**: O(n) - single pass through array.
**Space Complexity**: O(1) - only use two variables.
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Find maximum profit from buying and selling stock once.
        
        Args:
            prices: List of stock prices by day
            
        Returns:
            Maximum profit possible, or 0 if no profit
        """
        # Track minimum price seen so far - best price to buy at
        # Start with infinity because any real price will be lower
        min_price = float('inf')
        
        # Track maximum profit seen so far - best profit we can make
        max_profit = 0
        
        # Go through each price - check each day
        for price in prices:
            # Update minimum price if current price is lower - found better buy price
            # This is the cheapest we can buy the stock
            min_price = min(min_price, price)
            
            # Calculate profit if we sell at current price - selling today
            # Profit = current price - lowest price we've seen (buy price)
            profit = price - min_price
            
            # Update maximum profit if current profit is better - track best profit
            # Keep the highest profit we've seen
            max_profit = max(max_profit, profit)
        
        # Return the maximum profit - best we can do
        return max_profit

