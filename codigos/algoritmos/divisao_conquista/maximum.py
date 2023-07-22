def maximum(array):
    if len(array) == 1:
        return array[0]
    else:
        middle = len(array) // 2
        left = maximum(array[:middle])
        right = maximum(array[middle:])
        return max(left, right)

# Example
array = [5, 2, 4, 1, 8, 6, 3, 7]
result = maximum(array)
print(result)