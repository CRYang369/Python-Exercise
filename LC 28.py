# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 15:42:04 2023

@author: Yang Cairong
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if haystack[i:i+len(needle)]==needle:
                return i
        return -1