def expt(b, n):
    if n==0: 
        return 1
    return b * expt(b, n-1)
b,n = map(int,input().split()) 
print(expt(b,n))