def isCyclic(g,n):
    v=[False]*n
    for i in g:
        if(v[i]==False):
            if(dfs(g,i,v,-1)==1):
                return 1
    return 0            
def dfs(g,s,v,p):
    v[s]=True
    #print(s)
    for i in g[s]:
        if(v[i]==False):
            if(dfs(g,i,v,s)==1):
                return 1
        elif(i!=p):
            return 1
    return 0        
            
