def binomial(n ,k):
    memo = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(k + 1):
            if j == 0 or i == j:
                memo[i][j] = 1
            elif 0 < j < i:
                memo[i][j] = memo[i - 1][j - 1] + memo[i - 1][j]

    return memo[n][k]

# Example
result = binomial(6, 3) 
print(result)