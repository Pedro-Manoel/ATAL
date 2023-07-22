num = int(input())
arrPair = []
arrOdd = []

for i in range(1, num + 1):
    if i % 2 == 0:
        arrPair.append(i)
    else:
        arrOdd.append(i)

if num == 1:
    print(1)
elif len(arrOdd) + len(arrPair) >= 2 and abs(arrOdd[0] - arrPair[-1]) > 1:
    print(*(arrPair + arrOdd))
else:
    print("NO SOLUTION")

num = int(input())

arr = [i for i in range(1, num + 1)]
arr.sort(key=lambda x: x % 2)

if all(abs(arr[i] - arr[i+1]) != 1 for i in range(len(arr)-1)) and num > 1:
    print(*arr)
else:
    print("NO SOLUTION")


