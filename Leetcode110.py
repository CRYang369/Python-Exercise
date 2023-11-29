# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 14:54:05 2023
Given a binary tree, determine if it is height-balanced
A height-balanced binary tree is defined as a binary tree in which the depth of 
the two subtrees of every node never differ by more than 1.

Helper function balanced returns the depth of the root if the tree is balance or else -1
if not balance.
A tree is not balance if either left or right subtree is not balance, or the difference 
in left and right subtree depths is greater than 1.
Time O(n) visit all nodes
Space O(n)

.
@author: Yang Cairong
"""
class TreeNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
    
class Solution:
    def isBalanced(self,root):
        def hight(tree):
            if not tree:
                return 0
            left_depth=hight(tree.left)
            right_depth=hight(tree.right)
            
            if left_depth==-1 or right_depth==-1:
                return -1
            
            if abs(left_depth-right_depth)>1:
                return -1

            return 1+max(left_depth,right_depth)
        return hight(root)!=-1
            
if __name__=="__main__":
    trNode=TreeNode(4)
    leftNode=TreeNode(5)
    rightNode=TreeNode(6)
    Node5=TreeNode(7)
    Node6=TreeNode(8)
    
    
    trNode.left=leftNode
    trNode.right=rightNode
    trNode.left.left=Node5
    trNode.right.left=Node6
    
    test=Solution()
    tstrs=test.isBalanced(trNode)
    print(tstrs)
            