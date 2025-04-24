while True:
    a, b, c = map(int, input().split())
    if (a, b, c) == (0, 0, 0):
        break
    arr = [a, b, c]  # <-- 여기 수정!
    arr.sort()
    if (arr[0]**2 + arr[1]**2) == arr[2]**2:
        print("right")
    else:
        print("wrong")