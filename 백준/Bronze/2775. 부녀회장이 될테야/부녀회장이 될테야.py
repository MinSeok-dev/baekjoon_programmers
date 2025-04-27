T = int(input())  # 테스트 케이스 수

# 각 테스트 케이스마다 실행
for _ in range(T):
    k = int(input())  # k층
    n = int(input())  # n호
    
    # DP 배열 초기화
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    
    # 0층 초기화 (0층 i호에 사람 수는 i명)
    for i in range(1, n + 1):
        dp[0][i] = i

    # 1층부터 k층까지 채우기
    for floor in range(1, k + 1):  # 1층부터 k층까지
        for room in range(1, n + 1):  # 1호부터 n호까지
            dp[floor][room] = dp[floor][room - 1] + dp[floor - 1][room]

    # 결과 출력
    print(dp[k][n])  # k층 n호의 사람 수
