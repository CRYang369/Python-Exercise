# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 10:55:36 2023

@author: Yang Cairong
"""

def count_coin_combinations(coins, amount):
    dp = [0] * (amount + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]

    return dp[amount]

# Example usage:
coins = [1, 2, 5]
amount = 5
print(count_coin_combinations(coins, amount))  # Output: 4 (combinations: [1, 1, 1, 1, 1], [1, 1, 1, 2], [1, 2, 2], [5])
