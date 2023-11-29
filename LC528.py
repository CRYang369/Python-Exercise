# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 15:54:48 2023

You are given a 0-indexed array of positive integers w where w[i] describes the weight 
of the ith index.

You need to implement the function pickIndex(), which randomly picks an index in the
 range [0, w.length - 1] (inclusive) and returns it. The probability of picking 
 an index i is w[i] / sum(w).

For example, if w = [1, 3], the probability of picking index 0 is 1 / (1 + 3) = 0.25
 (i.e., 25%), and the probability of picking index 1 is 3 / (1 + 3) = 0.75 (i.e., 75%).

Condition/Input:
Given an array w of positive integers,where w[i] describes the weight 
of index i.The given will be treated as the input parameter of constructor function __init__
What?
Write a function pickIndex which randomly picks an index in proportion to its weitht.
How?
Create a list of cumulative weights.Choose a random integer between 1 and the sum 
of all weithts.Binary search the cumulative list for the index where the random integer 
would be inserted and return that index.probability of choosing an index is proprotional
 to its weight.
Time O(nlogn) for number of weights n
Space O（n)
@author: Yang Cairong
"""
import random,bisect 
class Solustion:
    def __init__(self,w):
        self.cumulative=[]
        total=0
        for weight in w:
            total+=weight
            self.cumulative.append(total)
    def pickIndex(self):
        x=random.randint(1,self.cumulative[-1])
        '''
        using python bisect module bisece_left to find the location for x,where 
        all the values left to x are less than x and all the values right to x are 
        equal to or great than x.it's like the lower bound
        While bisect.bisect or bisect.bisect_right a little bit difference with bisect_left
        the values left to x are less than or equal to x and the values right to x are 
        all great than x.it'like the upper bound.
        Call the python module bisect is as below:
    
        return bisect.bisect_left(self.cumulative,x)
        '''
        # x=random.randint(1,self.cumulative[-1])   
        low,high=0,len(self.cumulative)-1
        while low<=high:
            mid= low+(high-low)//2            
            if x==self.cumulative[mid]:
                return mid            
            elif x<self.cumulative[mid]:
                high=mid-1
            else:
                low=mid+1            
        return low


 

if __name__=="__main__":
    w=[2,3,4,6]
    mypick=Solustion(w)
    print(mypick.pickIndex())
