N = int(input())
cards = list(map(int, input().split()))

M = int(input())
check_numbers = list(map(int, input().split()))

card_set = set(cards)

result = [1 if num in card_set else 0 for num in check_numbers]
print(" ".join(map(str, result)))