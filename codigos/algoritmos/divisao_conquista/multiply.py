def multiply(x, y):
    if x < 10 or y < 10:
        return x * y

    size = max(len(str(x)), len(str(y)))
    half_size = size // 2

    high_x, low_x = divmod(x, 10**half_size)
    high_y, low_y = divmod(y, 10**half_size)

    z0 = multiply(low_x, low_y)
    z1 = multiply((low_x + high_x), (low_y + high_y))
    z2 = multiply(high_x, high_y)

    return (z2 * 10**(2 * half_size)) + ((z1 - z2 - z0) * 10**half_size) + z0

# Example
result = multiply(123456789, 987654321)
print(result)
