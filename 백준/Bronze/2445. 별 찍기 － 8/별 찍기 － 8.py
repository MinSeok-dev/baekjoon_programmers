n = int(input())
a= "*"
for i in range(n):
    print(a*(1+i) + " "*2*(n-1-i) + a*(1+i))
for i in range(1, n):
    print(a*(n-i) + " "*2*i + a*(n-i))