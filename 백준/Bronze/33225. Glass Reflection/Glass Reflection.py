arr = input()
answer = []
for i in range(len(arr)-1):
    if arr[i] == arr[i+1]:
        answer.append(arr[i])

# 리스트의 요소들을 결합해서 출력
print(''.join(answer))