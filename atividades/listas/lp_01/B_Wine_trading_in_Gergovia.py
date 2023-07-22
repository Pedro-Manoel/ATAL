num = int(input())
results = []

while num != 0:
    offers = list(map(int, input().split()))

    work = 0
    wine = 0
    for i in range(num):
        wine += offers[i]
        work += abs(wine)

    results.append(work)

    num = int(input())

for result in results:
    print(result)