def fun(n):
 a1=1, a2=2, a3=3
 if n==1: return a1
 elif n==2: return a2
 elif n==3: return a3
 for i in range(4,n+1):
  a=a3+a2-2*a1
  a1=a2, a2=a3, a3=a
 return a
print(fun(int(input())))