import sys
from collections import deque
def bfs(maps):
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    count = 0

    queue = deque()
    for i in range(m):
        for j in range(n):
            if maps[i][j] == 1:
                queue.append((i, j))
                count += 1

                # bfs 탐색
                while queue:
                    x, y = queue.popleft()
                    for dx, dy in dirs:
                        nx = x + dx
                        ny = y + dy

                        if nx < 0 or nx >= m or ny < 0 or ny >= n:
                            continue
                        if maps[nx][ny] == 1:
                            maps[nx][ny] = 0
                            queue.append((nx, ny))

    return count

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().rstrip().split())
    maps = [[0] * n for _ in range(m)]

    for _ in range(k):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        maps[x][y] = 1
    
    print(bfs(maps))