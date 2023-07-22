def permutation_with_repetition(array, result, i):
  if len(array) == i:
    print(result)
  else:
    for j in range(len(array)):
          result[i] = array[j]
          permutation_with_repetition(array, result, i + 1)
          result[i] = 0 # backtrack

# Example
array = [1,2]
default_result = [0] * len(array)
start_index = 0

permutation_with_repetition(array, default_result, start_index) 
