def sum(n): 
 summ=0
 for i in reverced(n):
   summ += int(i)
   print(i+"=", end="")
 print(summ)
sum(input())