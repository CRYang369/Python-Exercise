# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 17:58:32 2023

@author: Yang Cairong
"""

def count_distinct_values(arr):
    if len(arr) < 3:
        return 0

    distinct_values = set([arr[0], arr[1]])
    count = 0

    for num in arr[2:]:
        if num not in distinct_values:
            count += 1

    return count

# Example usage
arr = [1, 2, 3, 4, 1, 3, 5]
result = count_distinct_values(arr)
print(result)  # Output: 3
