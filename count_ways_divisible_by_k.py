# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 13:52:23 2023

@author: Yang Cairong
"""

def count_ways_divisible_by_k(a, k):
    # # Step 1: Create a frequency dictionary to count occurrences of each remainder
    # count = {}
    # for num in a:
    #     remainder = num % k
    #     count[remainder] = count.get(remainder, 0) + 1
    
    # # Step 4: Calculate the number of ways for each remainder and sum them up
    # total_ways = 0
    # for remainder, freq in count.items():
    #     if remainder == 0:
    #         total_ways += freq * (freq - 1) // 2
    #     elif k - remainder in count:
    #         total_ways += freq * count[k - remainder]
    
    # return total_ways
 
    count =0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if (a[i]+a[j])%k==0:
                count+=1
    return count


# Example usage:
a = [1, 2, 3, 4, 5]
k = 2
result = count_ways_divisible_by_k(a, k)
print(result)  # Output: 4 (The pairs are: (1, 3), (2, 4), (3, 5), (1, 5))
