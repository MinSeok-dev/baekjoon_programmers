import string

arr = input().upper()  # 모든 문자를 대문자로 변환
alist = list(string.ascii_uppercase)

for alpha in alist:
    n = arr.count(alpha)  # 해당 알파벳이 몇 번 나왔는지 세기
    print(f"{alpha} | {'*' * n}")  # 결과 출력