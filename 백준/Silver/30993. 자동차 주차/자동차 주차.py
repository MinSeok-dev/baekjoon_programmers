def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# 입력 받기
N, A, B, C = map(int, input().split())

# 팩토리얼 계산
N_fact = factorial(N)
A_fact = factorial(A)
B_fact = factorial(B)
C_fact = factorial(C)

# 중복 순열 계산
result = N_fact // (A_fact * B_fact * C_fact)

# 결과 출력
print(result)