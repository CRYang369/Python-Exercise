# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 10:46:36 2023

@author: Yang Cairong
"""

class Solution:
    def exist(self, board, word) :
        m=len(board)
        n=len(board[0])
        path=set()
        
        def dfs(row,col,index):
            if index==len(word):
                return True
            if row<0 or row==m or col<0 or col==n or board[row][col]!=word[index]or\
            (row,col) in path:
                return False
            path.add((row,col))
            
            res=dfs(row+1,col,index+1) or\
            dfs(row-1,col,index+1) or\
            dfs(row,col+1,index+1) or\
            dfs(row,col-1,index+1) 
            path.remove((row,col))
            return res
        
        for i in range(m):
            for j in range(n):
                if dfs(i,j,0):
                    return True   
        return False
    
if __name__ == "__main__":

    test=Solution()    
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "SEE"
    print(test.exist(board, word))  # Output: true