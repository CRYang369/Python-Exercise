# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 10:52:23 2023

@author: Yang Cairong
"""
def coin_change(amount, coins):
    mod = 10**9 + 7
    dp = [0] * (amount + 1)  # dp[i] = ways to make the amount i using given coins.
    dp[0] = 1
    for coin in coins:
        for current_amount in range(coin, amount + 1):
            dp[current_amount] = (dp[current_amount] + dp[current_amount - coin]) % mod
    return dp[amount]

# Example usage:
coins = [1, 2, 5]
amount = 5
print(coin_change(amount, coins))  # Output: 4 (combinations: [1, 1, 1, 1, 1], [1, 1, 1, 2], [1, 2, 2], [5])
