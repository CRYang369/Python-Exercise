# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 08:32:45 2023
Determine if a Sudoku is valid,according to :Sudoku Puzzles.
The Rules:
empty cells are filled with the character '.'
Create a set of digits seen in each row,column and box.
False if any duplicates
Time O(n^2)
Space O(n)


@author: Yang Cairong
"""
class Solution:
    def isValidSudoku(self,board):
        for i in range(9):
            rowlst=[]
            
            for j in range(9):
                
                if board[i][j]!='.':
                    rowlst.append(board[i][j])   #same row
 
        
            rowlst_check=list(set(rowlst))

            if len(rowlst)!=len(rowlst_check) :
                return False    
        for i in range(9):
            
            columnlst=[]
            for j in range(9):
                             

                if board[j][i]!='.':
                    columnlst.append(board[j][i])  #same column   

            columnlst_check=list(set(columnlst))
            if  len(columnlst)!=len(columnlst_check) :
                return False     
        for i in range(0,9,3):
            for j in range(0,9,3):
                boxlst=[]
                for ki in range(i,i+3):
                    for kj in range( j,j+3):
                        if  board[ki][kj]!='.':
                            boxlst.append(board[ki][kj])  #same box
                boxlst_check=list(set(boxlst))
                if len(boxlst)!=len(boxlst_check):
                    return False 
        return True
 
if __name__=="__main__":
    board = [
 ["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
    s=Solution()

print(s.isValidSudoku(board))                   