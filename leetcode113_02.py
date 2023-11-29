# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 18:13:39 2023

@author: Yang Cairong
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution: 
    def pathSum(self, root: TreeNode, targetSum: int) -> list[list[int]]:

        result = []
        path = []
        self.dfs(root, targetSum, path, result)
        return result

    def dfs(self, node, target, path, result):
        if not node:
            return
        path.append(node.val)
        if not node.left and not node.right and node.val == target:
            return result.append(path)
        self.dfs(node.left, target - node.val, path[:], result)
        self.dfs(node.right, target - node.val, path[:], result)
        # path.pop()
    
if __name__=="__main__":
        
        # root=[5,4,8,11,None,13,4,7,2,None,None,5,1]
        left3=TreeNode(7,None,None)
        right3=TreeNode(2,None,None)
        left2=TreeNode(11,left3,right3)
        left1=TreeNode(4,left2,None)
        right_left1=TreeNode(13,None,None)
        right_left2=TreeNode(5,None,None)
        right_right2=TreeNode(1,None,None)
        right_right1=TreeNode(4,right_left2,right_right2)
        right1=TreeNode(8,right_left1,right_right1)
        root=TreeNode(5,left1,right1)

        left2=(11,left3,right3)
        targetSum=22
        test=Solution()
        print(test.pathSum(root, targetSum))