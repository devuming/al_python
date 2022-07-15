# 미로탈출
from collections import deque
def solution(n, m, matrix):
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    queue = deque()
    queue.append((0, 0))  # 시작점

    while queue:
        x, y = queue.popleft()

        for dir_x, dir_y in dir:
            nx = x + dir_x
            ny = y + dir_y

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            
            if matrix[nx][ny] == 1:
                queue.append((nx, ny))
                matrix[nx][ny] =  matrix[x][y] + 1
    print(matrix)
    return matrix[n - 1][m - 1]

print(solution(5, 6, [[1,0,1,0,1,0], [1, 1, 1, 1, 1, 1], [0,0,0,0,0,1], [1,1,1,1,1,1], [1,1,1,1,1,1]]))
print(solution(3, 3, [[1, 1, 1], [0, 0, 1], [0, 0, 1]]))