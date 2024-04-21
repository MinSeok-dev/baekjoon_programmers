n, m = map(int, input().split())
s = []

def dfs(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    for i in range(start, n + 1):
        s.append(i)
        dfs(i)  # 다음 숫자부터 시작하도록 재귀 호출
        s.pop()

dfs(1)  # 시작 숫자는 1부터 시작합니다.