num = int(input())

while True:
    print(num, end=' ')
    if num == 1:
        break
    elif num % 2 == 0:
        num //= 2
    else:
        num = (num * 3) + 1
