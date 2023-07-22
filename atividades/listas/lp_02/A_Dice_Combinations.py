def dice_comb(n, mod):
    array = [0] * (n + 1)
    array[0], array[1] = 1, 1

    for i in range(2, n + 1):
        for j in range(1, 7):
            if i >= j:
                array[i] = (array[i] + array[i - j]) % mod
            else:
                break

    return array[n]     

n = int(input())
mod = 10**9 + 7
print(dice_comb(n, mod))
