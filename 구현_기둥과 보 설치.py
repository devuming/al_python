# 기둥과 보 설치 _ 구현문제
# * 실패
def solution(n, build_frame):
    answer = []
    m = [[-1] * (n + 1) for _ in range(n + 1)]
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for build in build_frame:
        x, y, a, b = build

        if b == 1 and checkValid(m, y, x, a):        # 설치
            m[y][x] = a
        else:
            deleteFlag = True
            for dir_x, dir_y in dir:
                nx = x + dir_x
                ny = y + dir_y

                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                
                if not checkValid(m, ny, nx, a):
                    deleteFlag = False
                    break 
            if deleteFlag:
                m[y][x] = -1

    for y in range(len(m)):
        for x in range(len(m[y])):
            if m[y][x] > -1:
                a = m[y][x]
                answer.append([x, y, a])

    answer.sort(key = lambda x : (x[0], x[1], x[2]))

    return answer

def checkValid(m, row, col, a):
    left = -1
    right = -1
    bottom = -1
    bottom_right = -1

    if col > 0:
        left = m[row][col-1]
    if col + 1 < len(m):
        right = m[row][col+1]
    if row + 1 < len(m):
        bottom = m[row - 1][col]
        if col + 1 < len(m):
            bottom_right = m[row - 1][col + 1]

    if a == 0:  # 기둥설치
        if row == 0 and m[row][col] == -1:    # 바닥에 아무것도 설치안되어져있는 경우 설치가능
            return True
        elif left == 1 or right == 1 or bottom == 0:  # 보나 기둥 위에
            return True
    if a == 1:  # 보 설치
        if left == 1 and right == 1:     # 양옆 보 사이
            return True
        elif bottom == 0 or bottom_right == 0:    # 기둥하고 이어지면
            return True
    
    return False


print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]])) #[[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]
print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]])) #[[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]