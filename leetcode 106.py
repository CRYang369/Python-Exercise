# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 16:55:35 2023

@author: Yang Cairong
"""

# # Definition for a binary tree node.
# from collections import List
# from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder, postorder):
        if not postorder:
            return None
        root=TreeNode(postorder[-1])
        root_index=inorder.index(postorder.pop())  
        
        left_inorder=inorder[:root_index]
        right_inorder=inorder[root_index+1:]
        
        l_left=len(left_inorder)
        
        left_postorder=postorder[:l_left] #from the beginning to the len(left_order)-1
        right_postorder=postorder[l_left:] #from the length of left subtree to the last second one in postorder
        
        root.left=self.buildTree(left_inorder, left_postorder)
        root.right=self.buildTree(right_inorder, right_postorder)      
        return root
        
        
        