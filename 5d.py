def GCD(a,b):
 if(b==0):
  return a
 else:
  return GCD(b, a%b)
def LCM(a,b):
 LCM = (a*b)//GCD(a,b)
 return LCM
n,m = map(int,input().split())
print("GCD",GCD(n,m))
print("LCM",LCM(n,m)