import sys
from collections import deque
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
n, m = map(int, sys.stdin.readline().rstrip().split())
camp = []
visited = [[False] * m for _ in range(n)]
sx, sy = -1, -1
for i in range(n):
    c = list(sys.stdin.readline().rstrip())
    camp.append(c)
    if (sx, sy) == (-1, -1):
        for j in range(m):
            if c[j] == 'I':
                sx, sy = i, j

queue = deque([])
queue.append((sx, sy))
visited[sx][sy] = True

answer = 0
while queue:
    x, y = queue.popleft()
    if camp[x][y] == 'P':
        answer += 1

    for dx, dy in dirs:
        nx = x + dx
        ny = y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if not visited[nx][ny] and camp[nx][ny] != 'X':
            visited[nx][ny] = True
            queue.append((nx, ny))

if answer == 0:
    print('TT')
else:
    print(answer)
