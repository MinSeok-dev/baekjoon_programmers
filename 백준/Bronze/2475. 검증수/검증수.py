verification = list(map(int, input().split()))

answer = 0

for i in verification:
    if i == 0:
        pass
    elif i == 1:
        answer += 1
    else:
        answer += i**2
        
print(answer%10)