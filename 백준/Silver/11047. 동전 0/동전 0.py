n, money = map(int, input().split())
cnt = 0
coins = [int(input()) for _ in range(n)]
coins.sort(reverse = True)

for coin in coins:
    cnt += money//coin
    money = money%coin

print(cnt)