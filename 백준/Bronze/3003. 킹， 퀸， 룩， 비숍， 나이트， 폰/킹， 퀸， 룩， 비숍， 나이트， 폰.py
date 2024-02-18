answer = [1,1,2,2,2,8]

status = [int(x) for x in input().split()]

for idx, x in enumerate(answer):
    status[idx] = x - status[idx]
    print(status[idx], end = " ")