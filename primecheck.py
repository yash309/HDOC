from math import sqrt
def isprime(n):
    if(n<2 or (n%2==0 and n!=2)):
        return False
    root=int(sqrt(n))
    for i in range(3,root+1,2):
        if(n%i==0):
            return False
    return True
        
