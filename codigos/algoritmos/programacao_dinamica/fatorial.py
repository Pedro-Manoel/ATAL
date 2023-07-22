def fatorial(n):
    memo = [0] * (n + 1)
    memo[:2] = 1, 1

    for i in range(2, n + 1):
        memo[i] = i * memo[i - 1]

    return memo[-1]

# Example
result = fatorial(4)
print(result)