def fun(a,b,c):
 if b >= a and b <= c: 
  print(a, b, c)
 elif c >= a and c <= b:
  print(a, c, b)
 elif a >= b and a <= c:
  print(b, a, c)
 elif c >= b and c <= a:
  print(b, c, a)
 elif a >= c and a <= b: 
  print(c, a, b)
 elif b >= a and b <= a: 
  print(c, b, a)
a,b,c = map(int,input().split())
fun(a,b,c)