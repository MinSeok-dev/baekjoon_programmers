N = int(input())

for _ in range(N):
    n = int(input())
    x = list(map(int, input().split()))
    print(f'{min(x)} {max(x)}')