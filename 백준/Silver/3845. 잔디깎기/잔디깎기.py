import sys

def check_grass(nx, ny, w, x_coords, y_coords):
    # 가로 방향 검사
    x_coords.sort()
    now = 0
    for x in x_coords:
        if x - (w / 2) <= now:
            now = x + (w / 2)
        else:
            return "NO"
    
    if now < 75:
        return "NO"
    
    # 세로 방향 검사
    y_coords.sort()
    now = 0
    for y in y_coords:
        if y - (w / 2) <= now:
            now = y + (w / 2)
        else:
            return "NO"
    
    if now < 100:
        return "NO"
    
    return "YES"


def main():
    input = sys.stdin.read
    data = input().splitlines()
    index = 0
    result = []
    
    while True:
        # 첫 번째 줄 읽기
        nx, ny, w = map(float, data[index].split())
        nx, ny = int(nx), int(ny)
        
        if nx == 0 and ny == 0 and w == 0:
            break
        
        # x 좌표들 읽기
        x_coords = list(map(float, data[index + 1].split()))
        
        # y 좌표들 읽기
        y_coords = list(map(float, data[index + 2].split()))
        
        # 가로, 세로 방향 검사
        result.append(check_grass(nx, ny, w, x_coords, y_coords))
        
        # 다음 테스트 케이스로 이동
        index += 3
    
    sys.stdout.write("\n".join(result) + "\n")


if __name__ == "__main__":
    main()