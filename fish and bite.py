# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 10:15:13 2023

@author: Yang Cairong
"""

       
def max_fish_with_baits(fish, baits):
    fish.sort(reverse=True)
    baits.sort(reverse=True)
    max_fish_count = 0

    for bait in baits:
        count = min(3, len([f for f in fish if f > bait]))
        max_fish_count += count
        fish = fish[count:]

    return max_fish_count

# Example usage:
fish = [5, 3, 9, 2, 6, 1, 8]
baits = [3, 5, 1, 4, 2]
result = max_fish_with_baits(fish, baits)
print(result)  # Output: 6 (Using baits of size 3, 5, 1, 4, 2, we can catch 6 fish: [9, 8, 6, 5, 3, 2])

    