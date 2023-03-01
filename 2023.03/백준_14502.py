import sys
from collections import deque
n, m = map(int, sys.stdin.readline().rstrip().split())
maps = []
answer = 0
for _ in range(n):
    maps.append(list(map(int, sys.stdin.readline().rstrip().split())))

def bfs():
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque()
    tmp_maps = [map[:] for map in maps]

    # 바이러스 퍼트리기
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 2:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()

        for dx, dy in dir:
            nx = x + dx
            ny = y + dy

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if tmp_maps[nx][ny] == 0:
                tmp_maps[nx][ny] = 2
                queue.append((nx, ny))
    area = 0
    for map in tmp_maps:
        area += map.count(0)

    return area


def back(cnt):
    global answer
    if cnt == 3:
        answer = max(answer, bfs())
        return 

    for i in range(n):
        for j in range(m):
            if maps[i][j] == 0:
                maps[i][j] = 1
                back(cnt + 1)
                maps[i][j] = 0
                
back(0)
print(answer)
