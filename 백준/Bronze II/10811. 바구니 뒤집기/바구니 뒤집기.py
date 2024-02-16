N, M = map(int, input().split())
baskets = [x for x in range(1, N+1)]
tmp = []

for _ in range(M):
    change1, change2 = map(int, input().split())
    tmp = baskets[change1-1 : change2]
    tmp.reverse()
    baskets[change1-1 : change2] = tmp
for i in range(N):
    print(baskets[i], end = " ")