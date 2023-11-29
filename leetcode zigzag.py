# -*- coding: utf-8 -*-
"""
Created on Mon May  8 09:47:51 2023

@author: Yang Cairong
"""
class Solution:
    def convert(self,s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
    
        result = [''] * numRows
        index, step = 0, 1
    
        for char in s:
            result[index] += char
    
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
    
            index += step
    
        return ''.join(result)
if __name__=="__main__":
    test=Solution()
    s = "PAYPALISHIRING"
    numRows = 4
    print(test.convert(s,numRows))