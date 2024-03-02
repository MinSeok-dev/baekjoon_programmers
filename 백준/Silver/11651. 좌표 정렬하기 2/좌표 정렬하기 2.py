N = int(input())

arr = []

for _ in range(N):
    x, y = map(int, input().split())
    arr.append((x, y))


arr.sort(key=lambda point: (point[1], point[0]))


for point in arr:
    print(point[0], point[1])