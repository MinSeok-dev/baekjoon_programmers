total = int(input())
num = int(input())
sumprice = 0
for _ in range(num):
    price, cnt = map(int, input().split())
    sumprice += price*cnt
    
if sumprice == total:
    print("Yes")
else:
    print("No")