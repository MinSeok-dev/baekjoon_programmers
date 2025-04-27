def lcd(a,b):
    while b != 0:
        a, b = b, a%b
    return a

arr = list(map(int,input().split()))
arr.sort(reverse = True)
LCD = lcd(arr[0], arr[1])
print(LCD)
print((arr[0]*arr[1])//LCD)