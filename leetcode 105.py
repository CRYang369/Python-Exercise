# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 16:37:18 2023
Construct binary tree from preorder and inorder traversal
Given preorder and inorder traversal of a tree, construct the binary tree.
You may assume that deplicates do not exist in the tree.

Build until we reach stop value,initiallly None.
Take first preorder as root then recurse left until inorder is root value.
Then discard inorder and recurse right until final stop.
Time O(n)
Space O(n)

@author: Yang Cairong
"""
from collections import deque,List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]):
        q=deque(preorder)
        length=len(preorder)
        lookup={v:i for i,v in enumerate(inorder)}
        def recbuild(start,end):
            if start>end:  # normal case:start<=end, exit case start>end
                return None
            else:
                cand=q.popleft()  # get the root of the tree from the preorder 
                root=TreeNode(cand)  # use the root bulid a TreeNode
                middle=lookup[cand]   #look for the root 
                            #and get the index of the root from the inorder dictionary.
                root.left=recbuild(start,middle-1) #recrusively build the left tree
                root.right=recbuild(middle+1,end) #recrusively build the right tree
                return root
        return recbuild(0,length-1) 
                