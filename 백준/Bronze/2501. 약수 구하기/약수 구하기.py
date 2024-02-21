N, K = map(int, input().split())

divisors = []

for i in range(1, int(N**0.5)+1):
    if N % i == 0:
        divisors.append(i)
        if i != N // i:
            divisors.append(N // i)
divisors.sort()
print(divisors[K-1] if K <= len(divisors) else 0)