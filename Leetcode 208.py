# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 17:10:53 2023
A trie (pronounced as "try") or prefix tree is a tree data structure used to 
efficiently store and retrieve keys in a dataset of strings.
 There are various applications of this data structure, such as autocomplete
 and spellchecker.
Node stores dictionary mapping mapping letters to chils nodes.Array would use fixed
space regardless of actual nb children.
Note that node desen't explicitly store letter.
Time O(n) to create where n is total length of all words.
O(k) to search where n is total length of all
Space O(n)




@author: Yang Cairong
"""

class TrieNode:

    def __init__(self):
        self.children={}  # type: { current node:childnode}
        self.terminal=False
        
class Trie:
    def __init__(self):
        self.root=TrieNode()
        self.root.terminal=True #empty string is a whold word
    def insert(self, word: str) -> None:
        node=self.root
        for c in word:
            if c not in node.children:
                node.children[c]=TrieNode()
            node=node.children[c]

        node.terminal=True

    def search(self, word: str) -> bool:
        node=self.root
        for c in word:
            if c in node.children:
                node=node.children[c]
            else:
                return False
        return node.terminal
           

    def startsWith(self, prefix: str) -> bool:
        node=self.root
        for c in prefix:
            if c in node.children:
                node=node.children[c]
            else:
                return False
        return True
    
if __name__=="__main__":
    
        
        