# -*- coding: utf-8 -*-
"""
Created on Tue May  9 09:12:38 2023

@author: Yang Cairong
"""

class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            sign = -1
            x = abs(x)
        else:
            sign = 1
        
        result = 0
        
        while x > 0:
            last_digit = x % 10
            result = result * 10 + last_digit
            x = x // 10
        
        result *= sign
        
        if result < -2**31 or result > 2**31 - 1:
            return 0
        
        return result
    
if __name__=="__main__": 
    test=Solution()
    x = -1230   
    print(test.reverse(x))
            