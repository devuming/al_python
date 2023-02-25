from collections import deque

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]   # 상하좌우
def bfs_L(maps, start_x, start_y):
    visited = [[-1] * len(maps[0]) for _ in range(len(maps))]

    queue = deque()
    queue.append((start_x, start_y, 0))
    visited[start_x][start_y] = 0

    while queue:
        now = queue.popleft()
        cnt = now[2] + 1

        for dx, dy in dirs:
            nx = now[0] + dx
            ny = now[1] + dy

            if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
                continue
            if maps[nx][ny] == 'X':
                continue
            if maps[nx][ny] == 'L':
                return (nx, ny, cnt)
            if visited[nx][ny] > -1:
                continue
            visited[nx][ny] = cnt
            queue.append((nx, ny, cnt))
    return (0, 0, -1)

def bfs_E(maps, start_x, start_y):
    visited = [[-1] * len(maps[0]) for _ in range(len(maps))]

    queue = deque()
    queue.append((start_x, start_y, 0))
    visited[start_x][start_y] = 0

    while queue:
        now = queue.popleft()
        cnt = now[2] + 1

        for dx, dy in dirs:
            nx = now[0] + dx
            ny = now[1] + dy

            if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
                continue
            if maps[nx][ny] == 'X':
                continue
            if maps[nx][ny] == 'E':
                return cnt
            if visited[nx][ny] > -1:
                continue
            visited[nx][ny] = cnt
            queue.append((nx, ny, cnt))
    return -1

def solution(maps):
    answer = -1
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                x, y, cnt = bfs_L(maps, i, j)       # S->L
                cnt_E = bfs_E(maps, x, y)    # S->E
                
                if cnt == -1 or cnt_E == -1:
                    return -1
                else:
                    return cnt + cnt_E
    return answer

print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))  # 16
print(solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]))  # -1