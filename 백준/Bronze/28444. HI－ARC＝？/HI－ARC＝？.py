hiarc = list(map(int,input().split()))
a, b = 1, 1
for idx, i in enumerate(hiarc):
    if idx == 0 or idx == 1:
        a *= i
    else:
        b *= i

print(a-b)