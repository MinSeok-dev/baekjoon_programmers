# 입력 받기
a = int(input())  # 1번 옵션에 베팅된 비율 (0 < a < 100)

# 배당 비율 계산
option1_ratio = 100 / a
option2_ratio = 100 / (100 - a)

# 결과 출력 (소수점 9자리까지)
print(f"{option1_ratio:.9f}")
print(f"{option2_ratio:.9f}")