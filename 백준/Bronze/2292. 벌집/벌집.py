N = int(input())
k = 1
cnt = 1
while N > k:
    k += 6 * cnt
    cnt += 1
print(cnt)