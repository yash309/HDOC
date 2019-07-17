def ispair(a,l,r,b):
    while(l<r):
        if(a[l]+a[r]==b):
            return True
        elif(a[l]+a[r]>b):
            r-=1
        else:
            l+=1
    return False    
for _ in range (int(input())):
    x=int(input())
    a=list(map(int,input().split()))
    a.sort()
    b=int(input())
    c=0
    for i in range(x):
        if(ispair(a,i+1,x-1,b-a[i])):
            c=1
            print("YES")
            break
    if(c==0):
        print("NO")
            
            
