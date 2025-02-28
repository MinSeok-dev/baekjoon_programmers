octa = input()
decimal = int(octa, 8)  # 8진수를 10진수로 변환
binary = bin(decimal)[2:] #이때, 결과는 '0b' 접두어가 붙은 문자열입니다. 이를 제거하기 위해 [2:]를 사용하여 앞의 '0b'를 잘라냅니다.
print(binary)