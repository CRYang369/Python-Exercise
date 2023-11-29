class DSTree:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        self.res=None
        
    def evaluate(self,val):
        if not self.left and not self.right:
           return self.res   
        return self.left.evaluate(val) if val<=self.val else self.right.evaluate(val)

    def split(self,lval,rval):
        self.left=DSTree(lval)
        self.right=DSTree(rval)
        return self.left,self.right
 
# left child is less than or equal to parent node value return True

if __name__=="__main__":
    root=DSTree(7)   
    Node1,Node2=root.split(4,9)
    Node3,Node4=Node1.split(1,6)
    Node5,Node6=Node2.split(8,10)
    
    Node3.res = True
    Node4.res = False
    Node5.res = True
    Node6.res = False
 
    test=root.evaluate(3)
    print(test)
    print(Node1.left.val,Node1.right.val)
    print(Node2.left.val,Node2.right.val)
    print(Node3.res,Node4.res,Node5.res,Node6.res)

            
    
        