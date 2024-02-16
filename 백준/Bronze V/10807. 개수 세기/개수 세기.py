n = int(input())
arr = [int(x) for x in input().split()]
answer = int(input())
cnt = 0
for idx, x in enumerate(arr):
    if answer == x:
        cnt += 1
        
print(cnt)