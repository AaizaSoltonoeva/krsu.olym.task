time=int(input("enter time"))
h= time//3600
m=(time-3600*h)//60
s= time- h *3600 - m * 60
print(h, m, s)