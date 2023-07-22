def div_array(array):
    if len(array) == 1:
        return array[0]
    else:
        middle = len(array) // 2
        left = div_array(array[:middle])
        right = div_array(array[middle:])
        return left - right

# Example
array = [5, 2, 4, 1, 3, 6, 8, 7]
result = div_array(array) 
print(result)