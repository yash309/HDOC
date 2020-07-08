# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

from  collections import defaultdict
class Solution:
    def help(self,d,l,A):
        if(A==None):
            return
        d[l].append(A.val)
        self.help(d,l+1,A.left)
        self.help(d,l,A.right)
    def solve(self, A):
        d=defaultdict(list)
        self.help(d,0,A)
        l=[]
        for i in d:
            l.extend(d[i])
        return l        
            
