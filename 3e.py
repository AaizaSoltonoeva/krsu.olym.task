a,b,c = map(int,input().split())
k = 'YES'
l = 'NO'
if a <= b+c and b <= a+c and c<= a+b:
 print (k)
else:
 print(l)