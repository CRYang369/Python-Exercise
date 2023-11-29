# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 23:53:20 2023

@author: Yang Cairong
"""

def find_combinations(candidates, target):
    def backtrack(start, target, current_combination):
        if target == 0:
            result.append(list(current_combination))
            return
        elif target < 0:
            return

        for i in range(start, len(candidates)):
            current_combination.append(candidates[i])
            backtrack(i, target - candidates[i], current_combination)
            current_combination.pop()

    result = []
    candidates.sort()
    backtrack(0, target, [])
    return result

# Test case
soda_bottles = [2, 3, 5]
target_amount = 7
print(find_combinations(soda_bottles, target_amount))
