def powerSum(x, n, s, i):
    if s == x:
        return 1
    else:
        value = s + (i+1)**n
        if value <= x:
            return powerSum(x, n, value, i+1) + powerSum(x, n, s, i+1)
    return 0

x = int(input())
n = int(input())
print(powerSum(x, n, 0, 0))