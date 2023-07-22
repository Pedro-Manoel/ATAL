def longest_increasing_subsequence(array):
    n = len(array)
    memo = [1] * n

    for i in range(1, n):
        for j in range(i):
            if array[i] > array[j] and memo[j] + 1 > memo[i]:
                memo[i] = memo[j] + 1

    return max(memo)

# Example
result = longest_increasing_subsequence([-7, 10, 9, 2, 3, 8, 8, 1])
print(result)