def mergesort(a,p,r):
    m=(p+r)//2
    if(p<r):
        mergesort(a,p,m)
        mergesort(a,m+1,r)
        merge(a,p,m,r)
    #return a    
def merge(a,p,q,r):
    m=max(a)
    n1=q-p+1
    n2=r-q
    l=[]
    R=[]
    for i in range(n1):
        l.append(a[p+i])#0 based indexing
    for j in range(n2):
        R.append(a[j+q+1])
    l.append(-1)
    R.append(-1)
    i=0
    j=0
    for k in range(p,r+1):
        if(l[i]>=R[j]):
            a[k]=l[i]
            i+=1
        else:
            a[k]=R[j]
            j+=1
a=list(map(int,input().split()))    
print(a)
mergesort(a,0,len(a)-1)   
print(a)
        
