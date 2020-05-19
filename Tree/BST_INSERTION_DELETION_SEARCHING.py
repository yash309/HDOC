class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key
class BST:
    def search(self,root,key):
        if(root):
            if(root.val==key):
                return True
            if(root.val<key):
                return self.search(root.right,key)
            else:
                return self.search(root.left,key)
        return False 
    def insert(self,root,node):
        if(root==None): 
            root=node 
        else: 
            if(root.val<node.val): 
                if(root.right==None): 
                    root.right = node 
                else: 
                    self.insert(root.right, node) 
            else: 
                if(root.left==None): 
                    root.left=node 
                else: 
                    self.insert(root.left, node)
    def inorder(self,root): 
        if root: 
            self.inorder(root.left) 
            print(root.val) 
            self.inorder(root.right)   
    def suc(self,root):
        c=root.right
        while(c!=None and c.left!=None):
            c=c.left
        return c.val    
    def delete(self,root,key):
        if(root==None):
            return root
        if(root.val>key):
            root.left=self.delete(root.left,key)
        elif(root.val<key):
            root.right=self.delete(root.right,key)
        else:
            if(root.right==None):
                return root.left
            elif(root.left==None):
                return root.right
            else:
                s=self.suc(root)
                root.val=s
                root.right=self.delete(root.right,s)
        return root        
if __name__=="__main__":
    c=BST()
    r=Node(50)
    for _ in range(int(input())):
        a=Node(int(input()))
        c.insert(r,a)
    c.inorder(r) 
    print("hh")
    c.delete(r,70)
    c.inorder(r) 
    print(c.search(r,50))
        
        
