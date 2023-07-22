def count_split_inversions(array, left, right):
    left.append(float('inf'))
    right.append(float('inf'))
    i = 0
    j = 0
    count = 0
    for k in range(len(array)):
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
            count += len(left) - i - 1
    return count
    
def count_inversions(array):
    if len(array) == 1:
        return 0
    else:
        middle = len(array) // 2
        left = array[:middle]
        right = array[middle:]
        left_count = count_inversions(left)
        right_count = count_inversions(right)
        split_count = count_split_inversions(array, left, right)
        return left_count + right_count + split_count
    
# Example
array = [8,3,2,9,7,1,5,4]
count = count_inversions(array)
print(count)