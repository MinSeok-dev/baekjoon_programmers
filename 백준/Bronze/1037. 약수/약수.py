N = int(input())

if N % 2 == 0:
    arr = [int(x) for x in input().split()]
    arr.sort()
    point = len(arr)//2
    print(arr[point-1]*arr[point])
else:
    arr = [int(x) for x in input().split()]
    arr.sort()
    if len(arr) == 1:
        print(arr[0]*arr[0])
    else:
        point = len(arr)//2 + 1
        print(arr[point-1]*arr[point-1])