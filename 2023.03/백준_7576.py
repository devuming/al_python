# 토마토
import sys
from collections import deque
def bfs(pos):
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque(pos)
    answer = 0
    while queue :
        x, y, date = queue.popleft()
        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if tomato[nx][ny] == -1:
                continue
            if tomato[nx][ny] == 0:
                tomato[nx][ny] = date + 1
                queue.append((nx, ny, tomato[nx][ny]))
        answer = max(date, answer)
    for t in tomato:
        if 0 in t:
            return -1
    return date

m, n = map(int, sys.stdin.readline().rstrip().split())
tomato = []
for _ in range(n):
    tomato.append(list(map(int, sys.stdin.readline().rstrip().split())))
pos = []    # 익은 토마토 좌표
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            pos.append((i, j, 0))
print(bfs(pos))