# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 00:23:02 2023

@author: Yang Cairong
"""

def rotate_image(matrix):
    n = len(matrix)

    # Transpose the matrix (swap elements across the main diagonal)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row of the transposed matrix to get the final result
    for i in range(n):
        matrix[i] = matrix[i][::-1]

    return matrix

# Test case
a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

print(rotate_image(a))
