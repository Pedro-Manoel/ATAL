def is_valid(element, result):
  return element not in set(result)

def permutation(array, result, i):
  if len(array) == i:
    print(result)
  else:
    for j in range(len(array)):
        if is_valid(array[j], result):
          result[i] = array[j]
          permutation(array, result, i + 1)
          result[i] = 0 # backtrack

# Example
array = [1,2]
default_result = [0] * len(array)
start_index = 0

permutation(array, default_result, start_index) 
