n = int(input())
a = "*"

for i in range(n):
    print(" "*(n-1-i) + a + 2*a*i)