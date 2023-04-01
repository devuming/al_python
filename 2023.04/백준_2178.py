import sys
from collections import deque
n, m = map(int, sys.stdin.readline().rstrip().split())
maps = []
for _ in range(n):
    maps.append(sys.stdin.readline().rstrip())
    

visited = [[1] * m for _ in range(n)]

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
queue = deque([(0, 0)])

while queue:
    x, y = queue.popleft()

    for dx, dy in dirs:
        nx = x + dx
        ny = y + dy

        if not (0 <= nx < n and 0 <= ny < m):
            continue   
        if maps[nx][ny] == '0':
            continue
        if visited[nx][ny] == 1:
            queue.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1

print(visited[n - 1][m - 1])