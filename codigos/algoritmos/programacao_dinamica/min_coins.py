def format_table(data, title):
    print(title)
    print("--------------------")
    for row in data:
        print(" ".join(str(cell).rjust(3) for cell in row))
    print("\n")

def get_used_coins(coins, n, memo):
    used_coins = []
    i = len(coins)
    j = n
    
    while i > 0 and j > 0:
        if memo[i][j] != memo[i - 1][j]:
            used_coins.append(coins[i - 1])
            j -= coins[i - 1]
        else:
            i -= 1
    
    return used_coins

def min_coins(coins, n):
    memo = [[0] * (n + 1) for _ in range(len(coins) + 1)]
    
    for i in range(len(coins) + 1):
        for j in range(n + 1):
            coin = coins[i - 1]
            if i == 0 or j == 0:
                memo[i][j] = 0
            elif coin == 1:
                memo[i][j] = j
            elif coin > j:
                memo[i][j] = memo[i - 1][j]
            else:
                memo[i][j] = min(memo[i - 1][j], memo[i][j - coin] + 1)
    
    return memo

# Example
coins = [1, 4, 6]
target_value = 8
memo = min_coins(coins, target_value)
used_coins = get_used_coins(coins, target_value, memo)

format_table(memo, "Coins Table")

print("Used Coins:")
print(used_coins)