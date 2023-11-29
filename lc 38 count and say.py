# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 22:22:44 2023

@author: Yang Cairong
"""

class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        def say(s):
            res=[]
            i=0
            while i<len(s):
                count=1
                while i+1<len(s) and s[i]==s[i+1]:
                    count+=1
                    i+=1
                res.append(str(count)+s[i])
                i+=1
        
            return "".join(res)
        prev_sequence='1'
        for _ in range(2,n+1):
            prev_sequence=say(prev_sequence)
        return prev_sequence