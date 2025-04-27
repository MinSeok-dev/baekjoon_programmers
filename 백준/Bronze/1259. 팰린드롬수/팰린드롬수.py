while True:
    num = input()
    if num == "0":
        break
    arr = [int(x) for x in num]
    if len(num)%2 == 1:
        half1 = arr[:len(num)//2]
        half2 = arr[len(num)//2+1:][::-1]
        if half1 == half2:
            print("yes")
        else:
            print("no")
    else:
        half1 = arr[:len(num)//2]
        half2 = arr[len(num)//2:][::-1]
        if half1 == half2:
            print("yes")
        else:
            print("no")