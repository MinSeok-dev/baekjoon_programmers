def calculate_min_rectangle_area(N, points):

    x_coordinates = [point[0] for point in points]
    y_coordinates = [point[1] for point in points]

    min_x = min(x_coordinates)
    max_x = max(x_coordinates)
    min_y = min(y_coordinates)
    max_y = max(y_coordinates)


    rectangle_area = (max_x - min_x) * (max_y - min_y)

    return rectangle_area


N = int(input())
points = []
for _ in range(N):
    x, y = map(int, input().split())
    points.append((x, y))

result = calculate_min_rectangle_area(N, points)
print(result)