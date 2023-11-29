# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 17:29:19 2023

@author: Yang Cairong
"""

def flip(num):
    flipper = int(''.join(str(num)[::-1]))
    if num == flipper:
        ans = False
    else:
        ans = True
    return (flipper, ans)

def is_asacending(numbers):
    res = all(x<y for x,y in zip(numbers, numbers[1:]))
    return res

def solution(numbers):
    if is_asacending(numbers)==True:
        return True
    else:
        NewList = []
        ans = []
        for num in numbers:
            CopyList = numbers.copy()
            y = numbers.index(num)
            CopyList[y] = flip(num)[0]
            NewList.append(CopyList)
            if is_asacending(CopyList):
                ans.append(True)
            else:
                ans.append(False)
        if True in ans:
            return True
        else:
            return False

#check with this
print(solution([1,5,10,20]))
print(solution([1,3,900,10]))
print(solution([13,31,30]))
print(solution([222,214,333]))