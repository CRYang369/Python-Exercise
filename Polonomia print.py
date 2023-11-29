# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 14:53:23 2023

@author: Yang Cairong
"""

ITEMS=6
def printPoly(poly,items):
    maxExp=poly[0]
    for i in range(1,poly[0]+2):
        maxExp-=1
        if poly[i]!=0:
            if (maxExp+1)!=0:
                print('%dX^%d' %(poly[i],maxExp+1),end='')
            else:
                print('%d' %poly[i],end='')
            if maxExp>=0:
                print('%c'%'+',end='')
    print()
    
polyA=[4,3,7,0,6,2]
printPoly(polyA,ITEMS)
                