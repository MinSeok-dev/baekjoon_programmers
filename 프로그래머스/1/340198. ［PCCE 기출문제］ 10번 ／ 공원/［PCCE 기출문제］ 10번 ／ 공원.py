def check_mat(mat_size, rows, cols, row, col, park):
    if row + mat_size > rows or col + mat_size > cols:
        return False
    
    for i in range(row, row+mat_size):
        for j in range(col, col+mat_size):
            if park[i][j] != "-1":
                return False
    return True

def find_mat(mat_size, park, rows, cols):
    for r in range(rows):
        for c in range(cols):
            if check_mat(mat_size, rows, cols, r, c, park):
                return True
    return False

def solution(mats, park):
    answer = -1
    mats.sort(reverse = True)
    
    rows = len(park)
    cols = len(park[0])
    
    for mat_size in mats:
        if find_mat(mat_size, park, rows, cols):
            return mat_size
    return answer