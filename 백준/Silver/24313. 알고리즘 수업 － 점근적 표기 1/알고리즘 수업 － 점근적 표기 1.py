
x1, x0 = map(int, input().split())
c = int(input())
n0 = int(input())
if ((x1*n0 + x0 <= c*n0)) and (x1<=c):
    print(1)
else:
    print(0)