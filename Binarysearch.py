# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 17:08:57 2023

@author: Yang Cairong
"""
class BinarySearch:
    def searchInsert(self,nums,target):
        low,high=0,len(nums)-1
        while low<=high:
            mid= low+(high-low)//2
            
            if target<nums[mid]:
                high=mid-1
            elif target>nums[mid]:
                low=mid+1
            else:
                return mid
            
        return low
if __name__=="__main__":
    test=BinarySearch()
    print(test.searchInsert([1,3,5,6,8],5))