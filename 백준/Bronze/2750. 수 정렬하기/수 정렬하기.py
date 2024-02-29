N = int(input())
numbers = [int(input()) for _ in range(N)]


sorted_numbers = sorted(numbers)


for num in sorted_numbers:
    print(num)