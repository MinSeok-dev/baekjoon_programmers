row, column = map(int, input().split())

arrA = []
arrB = []
for _ in range(row):
    arr = [int(x) for x in input().split()]
    arrA.append(arr)
for _ in range(row):
    arr = [int(x) for x in input().split()]
    arrB.append(arr)

result = [[0]*column for _ in range(row)]

for i in range(row):
    for j in range(column):
        result[i][j] = arrA[i][j] + arrB[i][j]
        
for N in result:
    print(*N)