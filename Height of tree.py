def height(root):
    if(root==None):
        return 0
    a=height(root.left)
    b=height(root.right)
    return max(a,b)+1
