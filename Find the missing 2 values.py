# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 10:20:24 2023

@author: Yang Cairong
"""

def find_missing_numbers(arr):
    N = len(arr) + 2
    # sum of first N numbers
    total_sum = (N * (N + 1)) // 2
    for i in arr:
        total_sum -= i
    # we find the average and store the sum of first average numbers
    average = total_sum // 2
    sum_average = (average * (average + 1)) // 2
    x = 0
    # sum of all numbers from arr less than or equal to the average
    for i in arr:
        if i <= average:
            x += i
    # the result sum_average - x gives the smaller missing number
    # we obtain the larger number using this smaller number
    num1 = sum_average - x
    num2 = total_sum - num1
    result = [int(num1), int(num2)]
    return result

# Example usage:
arr = [1, 2, 5, 6, 7]  # The missing numbers are 3 and 4
print(find_missing_numbers(arr))  # Output: [3, 4]
