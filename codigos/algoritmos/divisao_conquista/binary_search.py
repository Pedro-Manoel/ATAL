def binary_search(array, left, right, num):
    if left > right:
        return -1
    else:
        middle = (left + right) // 2
        if array[middle] == num:
            return middle
        elif array[middle] > num:
            return binary_search(array, left, middle - 1, num)
        else:
            return binary_search(array, middle + 1, right, num)

# Example
array = [1, 2, 3, 4, 5, 6, 7, 8]
left_index = 0
right_index = len(array) - 1
search = 7

index = binary_search(array, left_index, right_index, search)
print(f'Index: {index} - Value: {array[index]}')