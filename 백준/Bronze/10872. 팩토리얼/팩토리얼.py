N = int(input())

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

if N == 0:
    print(1)
else:
    print(factorial(N))