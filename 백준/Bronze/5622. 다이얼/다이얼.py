dic = {'ABC': 3, 'DEF': 4, 'GHI': 5, 'JKL': 6, 'MNO': 7, 'PQRS': 8, 'TUV': 9, 'WXYZ': 10}
char = input()
answer = 0
for alpha in char:
    for key in dic:
        if alpha in key:
            answer += dic[key]
            break
    
print(answer)