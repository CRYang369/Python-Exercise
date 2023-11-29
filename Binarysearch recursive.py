# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 17:13:26 2023

@author: Yang Cairong
"""
class binarySearch:
    def __init__ (self,arr,x): 
        self.arr=arr
        self.x=x
        # 基本判断
    def search(self, l, r):    
        
        self.l=l
        self.r=r
        
        if self.r >=self.l: 
      
            mid = self.l + (self.r - self.l)//2
      
            # 元素整好的中间位置
            if arr[mid] == self.x: 
                return mid 
              
            # 元素小于中间位置的元素，只需要再比较左边的元素
            elif arr[mid] > x: 
                return self.search(self.l, mid-1) 
      
            # 元素大于中间位置的元素，只需要再比较右边的元素
            else: 
                return self.search(mid+1,self.r) 
      
        else: 
            # 不存在
            return self.l
        
if __name__=="__main__":  
    # 测试数组
    arr = [ 2, 3, 4, 10, 40 ] 
    x = 5
    myBnSobj= binarySearch(arr,x)
    
    # 函数调用
    result = myBnSobj.search(0, len(arr)-1) 
    print(result)
