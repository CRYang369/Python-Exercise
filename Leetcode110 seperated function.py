# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 15:08:33 2023

@author: Yang Cairong
"""
class TreeNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class Solution:
    def isBalanced(self,root):
        if not root:
            return True
        lh=height(root.left)
        rh=height(root.right)
        return lh>=0 and rh>=0 and lh-rh in [-1,0,1]
        # return height(root)!=-1   simple type of writing
    
def height(tree):
    if not tree:
        return 0
    else:
        lh=height(tree.left)
        rh=height(tree.right)
        
        if lh==-1 or rh==-1:
            return -1
        
        if lh-rh in [-1,0,1]:
            return 1+max(lh,rh)
        else:
            return -1
       
        
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
            