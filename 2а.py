A=input().split(" ")
for i in range(len(A)):
 A[i] = int (A[i])
sum= A[0]+A[1]+A[2]
pr=A[0]*A[1]*A[2]
sr=float(sum/3)
print(sum)
print(pr)
print(sr)