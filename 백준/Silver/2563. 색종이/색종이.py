# 초기화된 100x100 크기의 도화지 생성
canvas = [[0] * 100 for _ in range(100)]

# 입력받은 색종이의 수
n = int(input())

# 색종이의 좌표를 도화지에 표시
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            canvas[i][j] = 1

# 검은 영역의 넓이 계산
black_area = sum(row.count(1) for row in canvas)

print(black_area)