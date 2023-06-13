import sys
from collections import deque
n, m = map(int, sys.stdin.readline().rstrip().split())
maps = []
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
queue = deque()
for i in range(n):
    maps.append(list(map(int, sys.stdin.readline().rstrip().split())))

    for j in range(m):
        if maps[i][j] == 2:
            queue.append((i, j, 0))
            break
visited = [[0] * m for _ in range(n)]

while queue:
    x, y, dist = queue.popleft()
    for dx, dy in dirs:
        nx = x + dx
        ny = y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if maps[nx][ny] == 1 and visited[nx][ny] == 0:
            visited[nx][ny] = dist + 1
            queue.append((nx, ny, dist + 1))

for i in range(n):
    for j in range(m):
        if maps[i][j] == 1 and visited[i][j] == 0:
            print(-1, end=' ')
        else:
            print(visited[i][j], end=' ')
    print()