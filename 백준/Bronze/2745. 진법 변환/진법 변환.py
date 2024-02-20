def base_to_decimal(base_number, base):
    decimal_number = 0
    power = 0

    # 숫자를 뒤에서부터 하나씩 가져와서 10진법으로 변환
    for digit in reversed(base_number):
        if digit.isdigit():
            # 숫자인 경우
            decimal_number += int(digit) * (base ** power)
        else:
            # 알파벳인 경우
            decimal_number += (ord(digit) - ord('A') + 10) * (base ** power)

        power += 1

    return decimal_number

# 입력 받기
input_str = input().split()
base_number = input_str[0]
base = int(input_str[1])

# B진법 수 N을 10진법으로 변환
decimal_number = base_to_decimal(base_number, base)

# 결과 출력
print(decimal_number)