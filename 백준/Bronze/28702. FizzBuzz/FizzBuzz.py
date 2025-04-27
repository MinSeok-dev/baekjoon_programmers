def fizzbuzz_after_index(seq):
    # 숫자만 추출하고, 그 숫자가 있는 원래 인덱스를 저장
    numbers = []
    indices = []
    
    for index, item in enumerate(seq):
        if item.isdigit():  # 숫자인지 확인
            numbers.append(int(item))
            indices.append(index)
    
    # 가장 큰 숫자 찾기
    max_number = max(numbers)
    max_index = indices[numbers.index(max_number)]  # 가장 큰 숫자가 있던 원래 인덱스
    
    # 숫자에서 인덱스를 빼기
    result_number = max_number +( 3 - max_index)
    
    # FizzBuzz 규칙 적용
    if result_number % 3 == 0 and result_number % 5 == 0:
        return "FizzBuzz"
    elif result_number % 3 == 0:
        return "Fizz"
    elif result_number % 5 == 0:
        return "Buzz"
    else:
        return result_number
seq = [input().strip() for _ in range(3)]
print(fizzbuzz_after_index(seq))