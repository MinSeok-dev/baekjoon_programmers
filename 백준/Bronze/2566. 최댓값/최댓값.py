arr = [list(map(int, input().split())) for _ in range(9)]

bigN = -1
point = [0]*2

for i in range(9):
    for j in range(9):
        if arr[i][j] > bigN:
            bigN = arr[i][j]
            point[0] = i+1
            point[1] = j+1
print(bigN)
print(*point)