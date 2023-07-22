def format_table(data, title):
    print(title)
    print("--------------------")
    for row in data:
        print(" ".join(str(cell).rjust(3) for cell in row))
    print("\n")

def get_items(wi, vi, memo):
    items_added = []
    item_indices = []
    n = len(wi)
    i = n
    j = len(memo[0]) - 1

    while i > 0 and j > 0:
        if memo[i][j] != memo[i - 1][j]:
            items_added.append(i - 1)
            item_indices.append(i - 1)
            j -= wi[i - 1]
        i -= 1

    items_added.reverse()
    item_indices.reverse()
    items = [(i, wi[item], vi[item]) for i, item in zip(item_indices, items_added)]

    return items

def knapsack(w, wi, vi):
    n = len(wi)
    memo = [[0] * (w + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, w + 1):
            if i == 0 or j == 0:
                memo[i][j] = 0
            elif wi[i - 1] > j:
                memo[i][j] = memo[i - 1][j]
            else:
                memo[i][j] = max(memo[i - 1][j], memo[i - 1][j - wi[i - 1]] + vi[i - 1])

    return memo

# Example
knapsack_limit_weight = 5
knapsack_weight = [3, 2, 4, 1]
knapsack_value = [8, 3, 9, 6]

memo = knapsack(knapsack_limit_weight, knapsack_weight, knapsack_value)
items = get_items(knapsack_weight, knapsack_value, memo)

format_table(memo, "Knapsack Table")

print(f'Max value: {memo[-1][-1]}')
print("Items:")
print("Item  Weight  Value")
for item, weight, value in items:
    print(f'{item + 1}     {weight}       {value}')