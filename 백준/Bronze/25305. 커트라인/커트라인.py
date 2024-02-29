N, M = map(int, input().split())

arr = [int(x) for x in input().split()]

arr.sort()

print(arr[-M])