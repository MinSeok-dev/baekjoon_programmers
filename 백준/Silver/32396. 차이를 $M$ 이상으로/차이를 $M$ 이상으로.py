n, m = map(int, input().split())
INF = int(1e13)
array = list(map(int, input().split()))
answer = 0

# 수열에서 인접한 항들 간의 차이를 확인
for i in range(1, n):
    if m > abs(array[i] - array[i - 1]):  # 차이가 M 미만이라면
        array[i] += INF  # 하나의 항을 INF만큼 증가시켜 차이를 만듦
        answer += 1  # 수정 횟수 증가

print(answer)