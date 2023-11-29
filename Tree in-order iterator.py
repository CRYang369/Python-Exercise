# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 09:12:54 2023

@author: Yang Cairong
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self._push_left_subtree(root)

    def next(self):
        node = self.stack.pop()
        self._push_left_subtree(node.right)
        return node.val

    def hasNext(self):
        return len(self.stack) > 0

    def _push_left_subtree(self, node):
        while node:
            self.stack.append(node)
            node = node.left

# Example Usage
root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.right = TreeNode(2)
root.right.left=TreeNode(5)
root.right.right=TreeNode(6)

bst_iterator = BSTIterator(root)
while bst_iterator.hasNext():
    print(bst_iterator.next())
