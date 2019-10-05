"""n = int(input)
setlocale(LC_ALL,"rus")
if n==1 or n==12 or n==12 or n==14:
 print("Вам",n ,"лет")
else a =n%10:
 elif a==1:
 print("Вам",a ,"год")
elif a==2 or a==3 or a==4
 print("Вам",a ,"годa")
else:
 print("Вам",n ,"лет")"""


N = int(input())
a = N % 10
if (N>9)and(N<20)or(N>110)or(a>4)or(a==0):
 print("Вам",N,"лет.")
else:
 if a==1: print("Вам",N,"год.")
 else: print("Вам",N,"года.")