n = int(input())
i=1
while i<n:
  sqr=i*i
  if i<10:
    if sqr%10==i: print(str(i),"*",str(i),"=",sqr)
  elif i<100:
    if sqr%100==i: print(str(i),"*",str(i),"=",sqr)
  i+=1