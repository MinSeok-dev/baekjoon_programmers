import sys
sys.setrecursionlimit(100000)

def dfs(x, y):
    if dp[x][y] != -1:  # 이미 계산된 경우
        return dp[x][y]
    
    dp[x][y] = 1  # 현재 칸 포함
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # 상하좌우 탐색
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and forest[nx][ny] > forest[x][y]:
            dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)
    
    return dp[x][y]

# 입력 받기
n = int(input())
forest = [list(map(int, input().split())) for _ in range(n)]

dp = [[-1] * n for _ in range(n)]  # DP 배열 초기화
result = 0

# 모든 위치에서 최대 이동 칸 계산
for i in range(n):
    for j in range(n):
        result = max(result, dfs(i, j))

print(result)