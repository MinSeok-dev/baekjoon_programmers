n = int(input())
cow = []
lr = []
cnt = 0
for _ in range(n):
    a,b = map(int, input().split())
    if a not in cow:
        cow.append(a)
        lr.append(b)
    else:
        c = cow.index(a)
        if lr[c] != b:
            cnt += 1
            lr[c] = b
print(cnt)
    