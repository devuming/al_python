import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())

INF = 10e9
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))

dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
def bfs_dist(now_x, now_y, now_size):
    dist = [[-1] * n for _ in range(n)]
    queue = deque()
    queue.append((now_x, now_y))
    dist[now_x][now_y] = 0
    while queue:
        x, y = queue.popleft()

        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy
            
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if dist[nx][ny] == -1 and board[nx][ny] <= now_size:
                queue.append((nx, ny)) 
                dist[nx][ny] = dist[x][y] + 1
    return dist

def find_eat(dist, now_size):
    min_dist = INF
    min_x, min_y = INF, INF

    for i in range(n):
        for j in range(n):
            if -1 < dist[i][j] < min_dist and 1 <= board[i][j] < now_size:
                min_dist = dist[i][j]
                min_x, min_y = i, j
    if min_dist == INF:
        return None
    else:
        return min_x, min_y, min_dist
    
# 시작 위치 찾기
sx, sy = -1, -1
for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            sx, sy = i, j
            board[i][j] = 0
            break
    if (sx, sy) != (-1, -1):
        break

ate = 0
size = 2
now_x, now_y = sx, sy
result = 0
while True:
    value = find_eat(bfs_dist(now_x, now_y, size), size)
    if value == None:
        print(result)
        break
    now_x, now_y = value[0], value[1]
    result += value[2]
    board[now_x][now_y] = 0

    ate += 1
    if ate >= size:
        size += 1
        ate = 0