N=int(input())
h= N//3600
m=(N-3600*h)//60
s= N- h *3600 - m * 60
print(h, m, s)