quant = int(input())
nums = list(map(int, input().split()))

nums.sort()

cont = 1
for i in range(1, quant):
    if nums[i] != nums[i-1]:
        cont += 1

print(cont)
