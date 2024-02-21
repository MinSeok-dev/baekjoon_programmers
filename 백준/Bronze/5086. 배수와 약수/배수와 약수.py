while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    else:
        if A > B:
            if A/B == A//B:
                print('multiple')
            else:
                print('neither')
        else:
            if B/A == B//A:
                print('factor')
            else:
                print('neither')
            