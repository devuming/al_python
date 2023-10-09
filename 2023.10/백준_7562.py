import sys
from collections import deque
dirs = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    l = int(sys.stdin.readline().rstrip())
    now_x, now_y = map(int, sys.stdin.readline().rstrip().split())
    end_x, end_y = map(int, sys.stdin.readline().rstrip().split())

    visited = [[-1] * l for _ in range(l)]
    visited[now_x][now_y] = 0
    queue = deque([(0, now_x, now_y)])
    while queue:
        cnt, x, y = queue.popleft()
        if (x, y) == (end_x, end_y):
            break
        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= l or ny < 0 or ny >= l:
                continue
            if visited[nx][ny] > -1:
                continue
            visited[nx][ny] = cnt + 1
            queue.append((cnt + 1, nx, ny))
    print(visited[end_x][end_y])
