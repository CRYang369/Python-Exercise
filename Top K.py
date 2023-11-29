# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 10:04:10 2023

@author: Yang Cairong
"""

def top_k(arr, k):
    # Use a set to maintain elements in sorted order
    tree = set()

    # Add all elements to the set and keep it at size k
    for x in arr:
        tree.add(x)
        if len(tree) > k:
            tree.remove(min(tree))

    # Convert the set to a list and return it
    return list(tree)

# Example usage:
arr = [3, 1, 5, 2, 4, 5]
k = 3
print(top_k(arr, k))  # Output: [3, 4, 5]
