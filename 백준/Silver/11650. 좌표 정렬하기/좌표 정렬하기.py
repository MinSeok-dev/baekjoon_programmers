N = int(input())

arr = []

for _ in range(N):
    x, y = map(int, input().split())
    arr.append((x, y))


arr.sort()


for point in arr:
    print(point[0], point[1])

    