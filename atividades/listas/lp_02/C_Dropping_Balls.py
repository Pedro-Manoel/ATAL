def drop_balls(deep, balls):
    node = 1

    for _ in range(1, deep):
        if balls % 2 == 1:
            node = 2 * node  # turn left
            balls = (balls + 1) // 2
        else:
            node = 2 * node + 1  # turn right
            balls = balls // 2
    
    return node

n = int(input())
for _ in range(n):
    deep, balls = map(int, input().split())
    print(drop_balls(deep, balls))
minus_one = int(input())
