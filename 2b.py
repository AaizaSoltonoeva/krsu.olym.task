A=input()
A=A.split()
B=input()
B=B.split()
x1,y1,x2,y2 = map(float)
from math import sqrt 
d= sqrt((x1-x2)**2 +(y1-y2)**2)
print(d)
