x=int(input())
b=bin(x)
b=b[2:]
c=1
#print(b)
for i in range(len(b)-1,-1,-1):
    #print(i)
    if(b[i]=="0"):
        f=len(b)-1-i
        c=0
        break
#print(f)    
if(c==1):
    f=len(b)
print(2**(f))
