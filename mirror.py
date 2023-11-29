# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 11:04:46 2023

@author: Yang Cairong
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def mirror_image(root):
    root = mirror_image_util(root)

def mirror_image_util(root):
    if not root:
        return root

    left = mirror_image_util(root.left)
    right = mirror_image_util(root.right)

    # Swap the left and right pointers.
    root.left = right
    root.right = left
    return root
# Original binary tree
#      1
#     / \
#    2   3
#   / \   \
#  4   5   6

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

mirror_image(root)

# Mirror tree
#      1
#     / \
#    3   2
#   /   / \
#  6   5   4
