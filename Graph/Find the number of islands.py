import sys
sys.setrecursionlimit(1000000)
def dfs(a,i,j,v,n,m):
    if(i>=0 and j>=0 and i<n and j<m):
        s=a[i][j]
        if(s==1 and v[i][j]==False):
            v[i][j]=True
            dfs(a,i-1,j,v,n,m)
            dfs(a,i,j-1,v,n,m)
            dfs(a,i-1,j-1,v,n,m)
            dfs(a,i-1,j+1,v,n,m)
            dfs(a,i+1,j-1,v,n,m)
            dfs(a,i+1,j,v,n,m)
            dfs(a,i,j+1,v,n,m)
            dfs(a,i+1,j+1,v,n,m)
def findIslands(a,n,m):
    l=[]
    v=[]
    c=0
    for i in range(m):
        l.append(False)
    for j in range(n):
        v.append(list(l))
    for i in range(n):
        for j in range(m):
            if(v[i][j]==False and a[i][j]==1):
                c+=1
                dfs(a,i,j,v,n,m)
    #print(v)            
    return c            
    #code here
