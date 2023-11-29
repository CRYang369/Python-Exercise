# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 17:21:29 2023

@author: Yang Cairong
"""
from collections import List
import itertools

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # Use set to store unique permutations
        unique_permutations = set()
        
        # Generate all permutations and add to set
        for permutation in itertools.permutations(nums):
            unique_permutations.add(permutation)
        
        # Convert set to list and return
        return list(unique_permutations)
