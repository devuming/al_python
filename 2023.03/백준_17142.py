# 연구소 3
import sys
from itertools import combinations
from collections import deque
n, m = map(int, sys.stdin.readline().rstrip().split())
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))

virus = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            virus.append((i, j))

virus_combi = list(combinations(virus, m))  # 바이러스 m 개만 활성화
min_sec = 10e9
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for v in virus_combi:
    queue = deque()
    visited = [[-1] * n for _ in range(n)]

    for x, y in v:
        queue.append((x, y, 0))
        visited[x][y] = 0
        
    second = 0  # 바이러스 걸리는데 걸리는 총 시간
    while queue:
        x, y, sec = queue.popleft() 
        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if board[nx][ny] == 1 or visited[nx][ny] > -1:
                continue
            # 바이러스 전파
            visited[nx][ny] = sec + 1
            queue.append((nx, ny, sec + 1))

            if board[nx][ny] == 0:
                second = max(second, sec + 1)

    # 방문안한 곳 있나 확인 = 모든 빈칸에 바이러스를 퍼트릴 수 없는 경우
    allFlag = True
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0 and visited[i][j] == -1:
                allFlag = False
                break
        if not allFlag:
            break

    if allFlag:    # 방문안한곳 있는지 확인
        min_sec = min(min_sec, second)  # 최소시간

if min_sec == 10e9:
    print(-1)
else:
    print(min_sec)