N = int(input("enter the number of angles"))
if N < 3:
 print ("Wrong! enter the number of angles")
elif N > 1000000:
 print ("Wrong! enter the number of angles")
else:
  sum = 180 * (N- 2)
  print(sum)