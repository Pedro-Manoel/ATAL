def maximum_subarray(array):
    max_current = max_global = array[0]

    for i in range(1, len(array)):
        max_current = max(array[i], max_current + array[i])
        max_global = max(max_global, max_current)

    return max_global

# Example
result = maximum_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(result)