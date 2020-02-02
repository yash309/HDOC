def qsort(A,P,R):
    if(P<R):
        q=partition(A,P,R)
        print(q)
        qsort(A,P,q-1)
        qsort(A,q+1,R)
def partition(a,p,r):
    x=a[r]
    i=p-1
    for j in range(p,r):
        if(x>a[j]):
            i+=1
            a[i],a[j]=a[j],a[i]
    a[i+1],a[r]=a[r],a[i+1]
    print(a)
    return i+1
x=list(map(int,input().split()))
print(qsort(x,0,len(x)-1))
print(x)
