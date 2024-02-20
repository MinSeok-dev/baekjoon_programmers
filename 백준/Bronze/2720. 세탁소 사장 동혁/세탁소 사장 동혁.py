def goal(change):
    quarters = change // 25
    change %= 25
    dimes = change // 10
    change %= 10
    nickels = change // 5
    change %= 5
    pennies = change
    return quarters, dimes, nickels, pennies

T = int(input())

for _ in range(T):
    C = int(input())
    result = goal(C)
    print(*result)