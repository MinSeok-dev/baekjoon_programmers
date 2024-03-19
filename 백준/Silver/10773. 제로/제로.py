a = int(input())
answer = []
for _ in range(a):
    num = int(input())
    if num != 0:
        answer.append(num)
    else:
        if answer:
            answer.pop()
            
print(sum(answer))