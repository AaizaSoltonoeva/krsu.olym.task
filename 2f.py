x1,y1,x2,y2,x3,y3 = map(float, input().split())   
S=0.5*abs((x1-x3)*(y2-y3)-(x2-x3)*(y1-y3))
from math import sqrt
AB = sqrt((x2-x1)**2+(y2-y1)**2)
AC = sqrt((x3-x1)**2+(y3-y1)**2)
BC = sqrt((x3-x2)**2+(y3-y2)**2)
P=AB+ AC+ BC
print(P,S, sep=" ")