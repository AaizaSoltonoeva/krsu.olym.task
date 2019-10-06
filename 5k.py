def fun(n):
    a = 1
    b = 2
    result = 0
    if n % 2 != 0:
        while a <= n:
            result += a * (a + 2)
            a += 4
    elif n % 2 == 0:
        while b <= n:
            result += b * (b + 2)
            b += 4
    return result
print(fun(int(input())))