N, K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))


coins.sort(reverse=True)

count = 0
for coin in coins:
    # 현재 가치의 동전으로 K를 만들 수 있는 최대 개수를 사용합니다.
    count += K // coin
    # 남은 값은 현재 동전을 사용한 만큼 빼줍니다.
    K %= coin

print(count)
