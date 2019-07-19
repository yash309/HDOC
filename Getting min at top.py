d=dict()
def _push(a,n):
    global d
    min1=a[0]
    s=[]
    s.append(a[0])
    d[0]=min1
    for i in range(1,n):
        if(a[i]<min1):
            min1=a[i]
            d[i]=min1
        else:
            d[i]=min1
        s.append(a[i])        
    return s    
def _getMinAtPop(stack):
    for i in range(len(stack)-1,-1,-1):
        print(d[i],end=" ")    
