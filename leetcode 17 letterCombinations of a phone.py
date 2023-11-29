# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 20:42:54 2023

@author: Yang Cairong
"""

class Solution:
    def letterCombinations(self, digits) :
        
        if not digits:
            return []

        digit_to_letters = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        # def backtrack(index, path):
        #     if len(path) == len(digits):
        #         combinations.append(''.join(path))
        #         return

        #     current_digit = digits[index]
        #     letters = digit_to_letters[current_digit]

        #     for letter in letters:
        #         path.append(letter)
        #         backtrack(index + 1, path)
        #         path.pop()

        # combinations = []
        # backtrack(0, [])
        # return combinations
        
 

        def backtrack(index, path):
            if len(path) == len(digits):
                combinations.append(''.join(path))
                return

            current_digit = digits[index]
            letters = digit_to_letters[current_digit]

            for letter in letters:
                backtrack(index + 1, path+letter)
       

        combinations = []
        backtrack(0, "")
        return combinations

    
if __name__ == "__main__":
    digits = "23"
    test=Solution()

print(test.letterCombinations(digits))  # Output: ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
