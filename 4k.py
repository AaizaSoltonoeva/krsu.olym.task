a,b = map(int, input().split())
c = []
for i in range(a, b):
    for j in range(2, i):
        if i % j == 0: break
    else:
        print(i,end = ' ')