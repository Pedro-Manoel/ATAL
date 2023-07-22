def merge(array, left, right):
    left.append(float('inf'))
    right.append(float('inf'))
    i = 0
    j = 0
    for k in range(len(array)):
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
    
def merge_sort(array):
    if len(array) > 1:
        middle = len(array) // 2
        left = array[:middle]
        right = array[middle:]
        merge_sort(left)
        merge_sort(right)
        merge(array, left, right)

# Example
array = [5, 2, 4, 1, 3, 6, 8, 7]
merge_sort(array)
print(array)