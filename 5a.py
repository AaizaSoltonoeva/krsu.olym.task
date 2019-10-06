def fun(n):
 k = 128
 while k>0:
  print(n//k, end="")
  n = n%k
  k=k//2
n = int(input())
fun(n)
