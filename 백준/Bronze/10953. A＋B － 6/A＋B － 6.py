import sys
n = int(sys.stdin.readline())

for _ in range(n):
    answer = list(map(int, sys.stdin.readline().split(",")))
    print(sum(answer))