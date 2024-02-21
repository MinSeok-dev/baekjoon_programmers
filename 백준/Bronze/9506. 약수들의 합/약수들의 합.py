while True:
    N = int(input())
    if N == -1:
        break
    factors = []
    for i in range(1, int(N**0.5)+1):
        if N % i == 0:
            factors.append(i)
            if i != N//i:
                factors.append(N//i)
    factors.sort()
    
    if sum(factors[:-1]) == N:
        print(f"{N} = {' + '.join(map(str, factors[:-1]))}")
    else:
        print(f'{N} is NOT perfect.')