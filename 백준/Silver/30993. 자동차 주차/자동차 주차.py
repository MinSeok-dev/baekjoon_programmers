import math

n, a, b, c = map(int,input().split())

answer = math.factorial(n)//(math.factorial(a)*math.factorial(b)*math.factorial(c))

print(answer)