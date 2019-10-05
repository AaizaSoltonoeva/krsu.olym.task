a,b,c=map(int,input().split())
sum = a+b+c
pr = a* b* c
sr=float(sum/3)
print(a,"+",b,"+",c,"=",sum)
print(a,"*",b,"*",c,"=",pr)
print("(",a,"+",b,"+",c,")/",3,"=",round(sr,3))