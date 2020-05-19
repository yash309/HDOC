class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key
    def insert(root,node):
        if(root==None): 
            root=node 
        else: 
            if(root.val<node.val): 
                if(root.right==None): 
                    root.right = node 
                else: 
                    Node.insert(root.right, node) 
            else: 
                if(root.left==None): 
                    root.left=node 
                else: 
                    Node.insert(root.left, node)
    def inorder(root): 
        if root: 
            Node.inorder(root.left) 
            print(root.val) 
            Node.inorder(root.right)   
    def search(root,key):
        if(root):
            if(root.val==key):
                return True
            if(root.val<key):
                return Node.search(root.right,key)
            else:
                return Node.search(root.left,key)
        return False 
    def suc(root):
        c=root.right
        while(c!=None and c.left!=None):
            c=c.left
        return c.val    
    def delete(root,key):
        if(root==None):
            return root
        if(root.val>key):
            root.left=Node.delete(root.left,key)
        elif(root.val<key):
            root.right=Node.delete(root.right,key)
        else:
            if(root.right==None):
                return root.left
            elif(root.left==None):
                return root.right
            else:
                s=Node.suc(root)
                root.val=s
                root.right=Node.delete(root.right,s)
        return root        
if __name__=="__main__":
    c=Node
    r=Node(50)
    for _ in range(int(input())):
        a=Node(int(input()))
        Node.insert(r,a)
    Node.inorder(r) 
    print("hh")
    Node.delete(r,70)
    Node.inorder(r) 
    print(c.search(r,100))
        
        
