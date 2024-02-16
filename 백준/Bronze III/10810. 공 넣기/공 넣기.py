N, M = map(int, input().split())
baskets = [0]*N

for _ in range(M):
    start, end, ball = map(int, input().split())
    for i in range(start -1, end):
        baskets[i] = ball

for i in range(N):
    print(baskets[i], end = " ")