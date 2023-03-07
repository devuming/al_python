import sys
from collections import deque
n, l, r = map(int, sys.stdin.readline().rstrip().split())
maps = []
for _ in range(n):
    maps.append(list(map(int, sys.stdin.readline().rstrip().split())))



def bfs(i, j, countries):
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    queue = deque()

    visited[i][j] = True
    queue.append((i, j))
    sum_value = maps[i][j]
    cnt = 1
    
    while queue:
        x, y = queue.popleft()

        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if visited[nx][ny]:     # 이미 방문한 곳인 경우
                continue
            if l <= abs(maps[x][y] - maps[nx][ny]) <= r:
                visited[nx][ny] = True     # 방문 표시
                queue.append((nx, ny))
                sum_value += maps[nx][ny]
                cnt += 1
                countries.append((nx, ny))
                
    return sum_value // cnt

answer = 0
while True:
    isMoved = False
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                countries = [(i, j)]
                count = bfs(i, j, countries)

                # 인구 수 갱신
                if len(countries) > 1:
                    isMoved = True
                    for cx, cy in countries:
                        maps[cx][cy] = count
    if isMoved:
        answer += 1
    else:
        break
print(answer)