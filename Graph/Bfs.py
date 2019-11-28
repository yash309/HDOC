def bfs(g,N):
    vis=[False]*N
    q=[]
    vis[0]=True
    q.append(0)
    while q:
        s=q.pop(0)
        print(s,end=" ")
        for j in g[s]:
            if(vis[j]==False):
                vis[j]=True
                q.append(j)
    '''
    can use queue module already imported
    :param g: given adjacency list of graph
    :param N: number of nodes in N.
    :return: print the bfs of the graph from node 0, newline is given by driver code
