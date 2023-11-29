# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 11:06:15 2023

@author: Yang Cairong
"""

def find_magic_triplets(arr):
    n = len(arr)
    arr.sort()  # Sort the array to make use of two-pointer technique

    triplets = []
    for i in range(n - 2):
        # Skip duplicates for the first element of the triplet
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        left, right = i + 1, n - 1
        while left < right:
            total_sum = arr[i] + arr[left] + arr[right]

            if total_sum == 0:
                triplets.append([arr[i], arr[left], arr[right]])

                # Skip duplicates for the second element of the triplet
                while left < right and arr[left] == arr[left + 1]:
                    left += 1
                # Skip duplicates for the third element of the triplet
                while left < right and arr[right] == arr[right - 1]:
                    right -= 1

                left += 1
                right -= 1
            elif total_sum < 0:
                left += 1
            else:
                right -= 1

    return triplets

# Example usage:
arr = [-1, 0, 1, 2, -1, -4]
print(find_magic_triplets(arr))  # Output: [[-1, -1, 2], [-1, 0, 1]]
