import sys

n, m = map(int, sys.stdin.readline().split())  # 빠른 입력 사용
elements = list(map(int, sys.stdin.readline().split()))

prefix = [0] * (n + 1)
for i in range(1, n + 1):
    prefix[i] = prefix[i - 1] + elements[i - 1]
    
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    print(prefix[y] - prefix[x - 1])