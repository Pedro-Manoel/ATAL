def heap_permutation(array, n):
    if n == 1:
        print(array)
    else:
        for i in range(n):
            heap_permutation(array, n - 1)
            j = 0 if n % 2 == 1 else i
            array[j], array[n - 1] = array[n - 1], array[j]

# Example
array = [1, 2]
n = len(array)
heap_permutation(array, n) 

