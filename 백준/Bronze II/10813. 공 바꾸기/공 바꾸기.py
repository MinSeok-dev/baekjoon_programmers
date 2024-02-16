N, M = map(int, input().split())
baskets = [x for x in range(1, N+1)]
tmp = 0

for _ in range(M):
    change1, change2 = map(int, input().split())
    tmp = baskets[change1-1]
    baskets[change1-1] = baskets[change2-1]
    baskets[change2-1] = tmp
for i in range(N):
    print(baskets[i], end = " ")