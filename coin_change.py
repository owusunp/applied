"""
LeetCode #322 - Coin Change

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: coins = [1,3,4], amount = 6
Output: 2
Explanation: 6 = 3 + 3

Example 2:
Input: coins = [2], amount = 3
Output: -1
Explanation: The amount of 3 cannot be made up with coins of value 2.

Example 3:
Input: coins = [1], amount = 0
Output: 0

Constraints:
- 1 <= coins.length <= 12
- 1 <= coins[i] <= 2^31 - 1
- 0 <= amount <= 10^4

THOUGHT PROCESS FOR INTERVIEWER:

**Approach**: Build up the solution step by step, starting from small amounts.

**How it works**:
- Start with amount 0 (needs 0 coins)
- For each amount from 1 to target, figure out the minimum coins needed
- Try using each coin - if the coin fits, see if it gives us a better solution
- Keep track of the best solution we've found so far

**Step by step**:
- For amount 0: we need 0 coins
- For amount 1: try coin 1 → need 1 coin total
- For amount 2: try coin 1 → need 2 coins total  
- For amount 3: try coin 3 → need 1 coin total (better than using three 1-coins)
- Keep going until we reach the target amount

**Example**: coins=[1,3,4], amount=6
- Amount 0: 0 coins
- Amount 1: 1 coin (use coin 1)
- Amount 2: 2 coins (use two coin 1s)
- Amount 3: 1 coin (use coin 3)
- Amount 4: 1 coin (use coin 4)
- Amount 5: 2 coins (use coin 1 + coin 4)
- Amount 6: 2 coins (use coin 3 + coin 3)

**Time**: We check each amount once and try each coin, so it's amount × number of coins.
"""

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Find minimum number of coins needed to make the amount using DP.
        
        Args:
            coins: List of coin denominations
            amount: Target amount to make
            
        Returns:
            Minimum coins needed, or -1 if impossible
        """
        # Initialize DP array with infinity - we use infinity because we want to find the minimum
        # and infinity represents "impossible to make this amount"
        dp = [float('inf')] * (amount + 1)
        # Set base case to 0 - we need 0 coins to make amount 0, this is our starting point
        dp[0] = 0
        
        # Build solution step by step - we start from small amounts and work our way up
        # because we need the solution for smaller amounts to solve larger amounts
        for i in range(1, amount + 1):  # Check each amount from 1 to target
            # Try each coin to see if it helps us make the current amount
            for coin in coins:
                # Only use coin if it's not bigger than the amount we're trying to make
                # because we can't use a coin worth more than the amount
                if coin <= i:
                    # Compare current best solution with using this coin
                    # dp[i-coin] is the minimum coins needed for the remaining amount
                    # +1 because we're using one more coin (the current coin)
                    # min() because we want the minimum number of coins
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        # Check if we found a solution - if dp[amount] is still infinity, it means impossible
        # Return -1 if impossible, otherwise return the minimum coins needed
        return dp[amount] if dp[amount] != float('inf') else -1
