# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 16:08:50 2023

@author: Yang Cairong
"""

def count_and_say(n):
    if n == 1:
        return "1"
    
    def say(s):
        result = []
        # for i in range(len(s)):
        i = 0
        while i < len(s):
            count = 1
            while i + 1 < len(s) and s[i] == s[i + 1]:
                i += 1
                count += 1
            result.append(str(count) + s[i])
            i += 1
        return ''.join(result)
    
    prev_sequence = "1"
    for _ in range(2, n + 1):
        prev_sequence = say(prev_sequence)
    
    return prev_sequence

# Example usage:
n = 7
print(count_and_say(n))  # Output: "13112221"
