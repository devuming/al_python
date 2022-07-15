# 음료수 얼려먹기 (BFS, DFS)
def solution_dfs(matrix, x, y):
    if x < 0 or y < 0 or x >= len(matrix) or y >= len(matrix[0]):
        return False
    if matrix[x][y] == 0:
        matrix[x][y] = 1    # 방문처리
        solution_dfs(matrix, x - 1, y)
        solution_dfs(matrix, x + 1, y)
        solution_dfs(matrix, x, y - 1)
        solution_dfs(matrix, x, y + 1)
        return True
    
    return False

from collections import deque
def solution_bfs(matrix, x, y, index):
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    queue = deque()
    matrix[x][y] = index
    queue.append((x, y))

    while queue:
        now = queue.popleft()

        for dir_x, dir_y in dir:
            nx = now[0] + dir_x
            ny = now[1] + dir_y

            if nx < 0 or ny < 0 or nx >= len(matrix) or ny >= len(matrix[0]):
                continue
            if matrix[nx][ny] == 0:
                matrix[nx][ny] = index
                queue.append((nx, ny))

from copy import deepcopy
def solution(n, m, matrix):
    ## DFS로 풀기
    dfs = deepcopy(matrix)
    result = 0
    for i in range(n):
        for j in range(m):
            if solution_dfs(dfs, i, j) == True:
                result += 1

    print("DFS : ", result)

    ## BFS로 풀기
    bfs = deepcopy(matrix)
    index = 1
    for i in range(n):
        for j in range(m):
            if bfs[i][j] == 0:
                index += 1
                solution_bfs(bfs, i, j, index)
    
    print("BFS : ", index - 1)
    
solution(4, 5, [[0, 0, 1, 1, 0], [0, 0, 0, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]) # 3
solution(15, 14, [  [0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
                    [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
                    [1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0],
                    [1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0],
                    [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
                    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
                    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
                    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
                    [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1],
                    [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
                    ])  # 8
solution(3, 3, [[0, 0, 1], [0, 1, 0], [1, 0, 1]])       # 3