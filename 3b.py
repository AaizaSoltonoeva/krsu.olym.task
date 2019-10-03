a,b,c = map(int, input().split())
if a>b and a>c:
 print('Anton')
elif b>c and b>a:
 print('Boris')
elif c>b and c>a:
 print('Victor')
elif a==b and b>c:
 print('Victor')
elif b==c and c>a:
 print('Anton')
elif c==a and a>b:
 print('Boris')
if a==b and b==c:
 print('Same age')