# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 23:08:34 2023

@author: Yang Cairong
"""
from collections import deque
class DecisionNode:
    def __init__(self,val,left=None,right=None):
        # result:dict):
        self.val=val
        # self.result=result #save the current brach result  
        self.left=left
        self.right=right
    def get_val(self):
        return self.val
    def set_val(self,val):
        self.val=val
    def get_left(self):
        return self.left
    def set_left(self,left):
        self.left=left
    def get_right(self):
        return self.right
    def set_right(self,right):
        self.right=right
        
class DecisionTreeClass:
    def __init__(self,lst):
        lst=sorted(lst)
        self.root=self.build_tree(lst)
    def build_tree(self,lst):
        
        l,r=0,len(lst)-1
        if(l>r):
            return None
        if(l==r):
            return DecisionNode(lst[1])
        mid=(l+r)//2
        root=DecisionNode(lst[mid])
        root.left=self.build_tree(lst[:mid])
        root.right=self.build_tree(lst[mid+1:])
        return root
    def preorder(self,root):
        if(root is None): # not root
            return
        print( root.val)
        self.preorder(root.left)
        self.preorder(root.right)
        
    def postorder(self,root):
        if(root is None):
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.val)
    
    def inorder(self,root):
        if(not root):
            return
        self.inorder(root.left)
        print (root.val)
        self.inorder(root.right)
        
    def levelorder(self,root):
        if (not root):
            return
        biqueue=deque([root])
        size=len(biqueue)
        for i in range(0,size):
            node=biqueue.popleft()
            print(node.val)
            if  node.left :
                biqueue.append(node.left)
            if node.right:
                biqueue.append(node.right)
                
if __name__=="__main__":
    list1=[1,-1,3,4,5]
    tree=DecisionTreeClass(list1)
    tree.inorder(tree.root)
    tree.preorder(tree.root)
    tree.postorder(tree.root)
    tree.levelorder(tree.root)
    
            
                
                
            
          
            
        
        
        
        
        

        