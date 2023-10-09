# 도화지의 그림의 갯수와, 가장 넓은 것의 넓이 출력
import sys
from collections import deque
n, m = map(int, sys.stdin.readline().rstrip().split())
paper = []
for _ in range(n):
    paper.append(list(map(int, sys.stdin.readline().rstrip().split())))

visited = [[False] * m for _ in range(n)]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
count = 0
max_area = 0
for i in range(n):
    for j in range(m):
        if paper[i][j] == 0 or visited[i][j]:
            continue
        count += 1
        area = 1
        queue = deque([(i, j)])
        visited[i][j] = True
        while queue:
            x, y = queue.popleft()

            for dx, dy in dirs:
                nx = x + dx
                ny = y + dy
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if paper[nx][ny] == 0 or visited[nx][ny]:
                    continue
                visited[nx][ny] = True
                queue.append((nx, ny))
                area += 1
        max_area = max(max_area, area)

print(count)
print(max_area)
