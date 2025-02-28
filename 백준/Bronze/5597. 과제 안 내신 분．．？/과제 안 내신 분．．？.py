a = [int(input()) for _ in range(28)]

for x in range(1,31):
    if x not in a:
        print(x)