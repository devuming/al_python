# 토마토2 
import sys
from collections import deque
def bfs(n, h, pos):
    dirs = [(-1, 0, True), (1, 0, True), (0, -1, True), (0, 1, True), (-n, 0, False), (n, 0, False)] # 위, 아래, 왼쪽, 오른쪽,
    queue = deque(pos)
    answer = 0
    while queue :
        x, y, date = queue.popleft()
        for dx, dy, sameBox in dirs:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= (n * h) or ny < 0 or ny >= m:
                continue
            start = (x // n) * n   # 층 시작 범위
            if sameBox and (nx < start or nx >= start + n):   # 상하좌우가 같은 층이 아닌 경우
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

m, n, h= map(int, sys.stdin.readline().rstrip().split())
tomato = []
for _ in range(n * h):
    tomato.append(list(map(int, sys.stdin.readline().rstrip().split())))
pos = []    # 익은 토마토 좌표
for i in range(n * h):
    for j in range(m):
        if tomato[i][j] == 1:
            pos.append((i, j, 0))
print(bfs(n, h, pos))
