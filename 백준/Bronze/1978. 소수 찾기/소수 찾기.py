def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def count_primes(numbers):
    count = 0
    for num in numbers:
        if is_prime(num):
            count += 1
    return count


N = int(input())
numbers = list(map(int, input().split()))

# 소수의 개수 세기
result = count_primes(numbers)

# 결과 출력
print(result)