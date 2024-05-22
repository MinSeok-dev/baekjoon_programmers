N, K = map(int, input().split())

if K > N//2:
    K = N-K
x, y = 1, 1
for i in range(1, K+1):
    x *= i
    y *= N
    N -= 1
print(y//x)