numbers = [int(input()) for _ in range(5)]


average = sum(numbers) // 5


sorted_numbers = sorted(numbers)
median = sorted_numbers[2]


print(average)
print(median)