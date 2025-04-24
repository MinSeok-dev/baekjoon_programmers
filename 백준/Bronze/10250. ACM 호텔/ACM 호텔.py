n = int(input())

for _ in range(n):
    h, w, c = map(int, input().split())
    
    floor = c % h
    if floor == 0:
        floor = h
    
    room = c // h + 1
    if c % h == 0:
        room -= 1  # 딱 나눠떨어질 때는 한 칸 당겨야 함

    room_number = str(floor) + str(room).zfill(2)  # 층수 + 두 자리 호수
    print(room_number)
    