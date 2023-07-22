def longest_common_subsequence(array1, array2):
    m = len(array1)
    n = len(array2)
    memo = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if array1[i - 1] == array2[j - 1]:
                memo[i][j] = memo[i-1][j-1] + 1
            else:
                memo[i][j] = max(memo[i-1][j], memo[i][j-1])

    return memo[-1][-1]

# Example
result = longest_common_subsequence([1, 2, 3, 2], [2, 4, 3, 1, 2]) 
print(result)