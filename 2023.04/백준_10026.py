import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())
maps = []
for _ in range(n):
    maps.append(sys.stdin.readline().rstrip())

def bfs(i, j, visited, color):
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(i, j)])
    while queue:
        x, y = queue.popleft()

        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if visited[nx][ny] or maps[nx][ny] not in color:
                continue
            queue.append((nx, ny))
            visited[nx][ny] = True

r_g_b = [[False] * n for _ in range(n)]
rg_b = [[False] * n for _ in range(n)]
cnt = [0, 0]

for i in range(n):
    for j in range(n):
        if not r_g_b[i][j]:
            bfs(i, j, r_g_b, [maps[i][j]])
            cnt[0] += 1
        if not rg_b[i][j]:    # 적록 색약
            if maps[i][j] in ['R', 'G']:
                bfs(i, j, rg_b,  ['R', 'G'])
            else:
                bfs(i, j, rg_b,  ['B'])
            cnt[1] += 1

print(cnt[0], cnt[1])