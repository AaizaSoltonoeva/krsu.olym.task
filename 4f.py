n = int(input())
result = "NO"
a = 0
b = 0
while n > 0:
    a = n%10
    b = n//10%10
    if a == b:
        result = "YES"
    n = n//10
print (result)