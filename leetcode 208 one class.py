'''
Node stores dictionary mapping letters to child nodes.
Array would use fixed space regardless of actural nb children.
Note that node doesn't explicityly store letter'

'''
        
class Trie:
    def __init__(self):
        self.root={}
        self.terminal="#"
        
    def insert(self, word: str) -> None:
        node=self.root
        for c in word:
            node=node.setdefault(c,{})
        node[self.terminal] =self.terminal

    def search(self, word: str) -> bool:
        node=self.root
        for c in word:
            if c in node:
                node=node[c]
            else:
                return False
        return self.terminal in node
           

    def startsWith(self, prefix: str) -> bool:
        node=self.root
        for c in prefix:
            if c in node:
                node=node[c]
            else:
                return False
        return True
    
if __name__=="__main__":
    
        
        