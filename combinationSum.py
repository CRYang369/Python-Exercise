# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 15:57:03 2023

@author: Yang Cairong
"""
def combinationSum(candidates, target):
    def backtrack(start, target, path):
        if target == 0:
            res.append(path)
            return
        for i in range(start, len(candidates)):
            if candidates[i] > target:
                continue
            backtrack(i, target - candidates[i], path + [candidates[i]])

    res = []
    candidates.sort()
    backtrack(0, target, [])
    return res


candidates = [2, 3, 6, 7]
target = 7
print(combinationSum(candidates, target))