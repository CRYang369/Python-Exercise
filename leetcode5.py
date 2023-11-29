# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 22:22:28 2023

@author: Yang Cairong
"""

class Solution:
    def longestPalindrome(self,s):
        # if s==None or len(s)<1: return ""
        # start,end=0,0
        # def expandFromMiddle(strings,left,right):
        #     if strings==None or left>right: return 0
        #     while left>=0 and right <len(strings) and strings[left]==strings[right]:
        #         left-=1
        #         right+=1
        #     return right-left-1
        
        # for i in range(len(s)):
        #     len1=expandFromMiddle(s,i,i) #odd
        #     len2=expandFromMiddle(s,i,i+1) #even
        #     length=max(len1,len2)
        #     if length>end-start:
        #         start=i-(length-1)//2
        #         end=i+length//2
        # return s[start:end+1]
        
        
        n=len(s)
        def getLen(l,r):
            while l>=0 and r<n and s[l]==s[r]:
                l-=1
                r+=1
            return r-l-1
        start=0
        length=0
        for i in range(n):
            cur=max(getLen(i,i), getLen(i,i+1))
            if cur<=length:continue
            length=cur
            start=i-(cur-1)//2
        return s[start:start+length]
    

if __name__=="__main__":
    test=Solution()
    s="abbacd"
    print(test.longestPalindrome(s))