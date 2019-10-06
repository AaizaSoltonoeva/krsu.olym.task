def gcd(c):       
 while a!=0 and b!= 0:
  if a>b:
   a=a%b 
  else:
   b=b%a
 c=a+b
a,b = map(int,input().split())
print ("GCD(",a,b, ")=",gcd(c)) 