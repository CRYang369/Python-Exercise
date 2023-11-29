# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 21:22:34 2023

@author: Yang Cairong
"""

class Solution:
    def isValidSudoku(self,board):
        rows=[{} for i in range(9)]
        columns=[{} for i in range(9)]
        boxes=[{} for i in range(9)]
        for i in range(9):
            for j in range(9):
                num=board[i][j]
                if num!='.':
                    num=int(num)
                    box_index=(i//3)*3+j//3
                    rows[i][num]=rows[i].get(num,0)+1
                    columns[j][num]=columns[j].get(num,0)+1
                    boxes[box_index][num]=boxes[box_index].get(num,0)+1
                    if rows[i][num]>1 or columns[j][num] >1 or boxes[box_index][num]>1:
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

print(s.isValidSodoku(board))