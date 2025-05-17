while True:
    B, N = map(int, input().split())
    if B == 0 and N == 0:
        break

    min_diff = float('inf')
    best_A = 0
    A = 1

    while True:
        power = A ** N
        diff = abs(power - B)
        
        if diff < min_diff:
            min_diff = diff
            best_A = A
        else:
            # 차이가 커지기 시작하면 그만 탐색
            break
        A += 1

    print(best_A)