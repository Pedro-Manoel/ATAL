def minimum(array):
    if len(array) == 1:
        return array[0]
    else:
        middle = len(array) // 2
        left = minimum(array[:middle])
        right = minimum(array[middle:])
        return min(left, right)

# Example
array = [5, 2, 4, 1, 8, 6, 3, 7]
result = minimum(array)
print(result)