N = int(input())
if N<0:
 print("ERROR")
else:
  sum=0; i=1; N1=0; N2=1; 
  while i<N:
   sum += i
   N1=N2; N2=i
   i=N1+N2
  print(sum)


