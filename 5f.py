def gcd(a,b): 
 while b !=0:
  if a>b:
   return gcd(b, a%b)
  elif a<b:
    return gcd(a, b%a)
 return a
 
a,b=map(int,input().split())
c=gcd(a,b)
print(str(a//c)+"/"+str(b//c))