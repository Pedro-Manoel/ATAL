def perm(array, length, i):
    if i == length:
        yield "".join(array)
    else:
        used = set()
        for j in range(i, length):
            if array[j] not in used:
                used.add(array[j])
                array[i], array[j] = array[j], array[i]
                yield from perm(array, length, i + 1)
                array[i], array[j] = array[j], array[i]  # backtrack

string = input()
results = list(perm(list(string), len(string), 0))
print(len(results))
for result in sorted(results):
    print(result)