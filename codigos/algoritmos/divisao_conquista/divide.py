def divide(x, y):
    if x < y:
        return 0
    elif x == y:
        return 1

    size = len(str(x)) - len(str(y))
    y_times_10_to_size = y * 10**size

    if y_times_10_to_size > x:
        size -= 1
        y_times_10_to_size = y * 10**size

    q = 0
    r = x
    while r >= y:
        r -= y_times_10_to_size
        q += 10**size
    return q + divide(r, y)

# Example
result = divide(1000, 25)
print(result)