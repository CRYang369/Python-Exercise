# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 17:09:48 2023

@author: Yang Cairong
"""
from collections import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        def subset(p, up):
            if len(up) == 0:
                if p not in ans:
                    ans.append(p)
                return 
            ch = up[0]
            for i in range(len(p) + 1):
                subset(p[0:i] + [ch] + p[i:], up[1:])
        subset([], nums)
        return ans
    
    
    '''
    The given code implements a function permuteUnique that takes a list of integers nums as input 
    and returns a list of all possible unique permutations of the elements in nums.

The function first sorts the input list nums. It then defines a nested function subset 
that recursively generates permutations. The subset function takes two arguments: p,
 which is the current permutation being constructed (initially an empty list), and up, 
 which is the list of integers that have not been used in the current permutation (initially the sorted nums list).

The subset function first checks if up is empty, in which case it adds the current permutation p
 to the answer list ans if it is not already present and returns. Otherwise, it chooses the first unused integer
 ch from up, and inserts it into all possible positions in the current permutation p using a loop. 
 It then recursively calls subset with the updated permutation and the remaining unused integers in up.

Finally, the subset function is called with an empty permutation and the sorted nums list to start the recursion, and the answer list ans is returned.

One potential issue with this implementation is that it uses a list to check for duplicate permutations, which can be inefficient for larger inputs. A more efficient way to check for duplicates would be to use a set or a dictionary.
    '''