n = int(input())
a = "*"
for i in range(n):
    print(" "*i + a + 2*a*(n-1-i))
