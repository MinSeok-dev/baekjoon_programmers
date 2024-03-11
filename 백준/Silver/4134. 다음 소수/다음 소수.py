import math

def solution(n):
    def is_prime(x):
        if x == 0 or x == 1:
            return False
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True

    while True:
        if is_prime(n):
            return n
        else:
            n += 1

N = int(input())

for _ in range(N):
    n = int(input())
    answer = solution(n)
    print(answer)