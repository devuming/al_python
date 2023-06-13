import sys
from collections import deque

answer = 0
n, m = map(int, sys.stdin.readline().rstrip().split())
board = []
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))

def checkCount():
    cnt = 0
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j] > 0 and not visited[i][j]:
                bfs(visited, i, j)
                cnt += 1

    return cnt

def bfs(visited, i, j):
    queue = deque([(i, j)])
    visited[i][j] = True

    while queue:
        x, y = queue.popleft()
        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if board[nx][ny] > 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))

while True:
    answer += 1
    bCount = []
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                continue
            cnt = 0
            for dx, dy in dirs:
                nx = i + dx
                ny = j + dy
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if board[nx][ny] == 0:
                    cnt += 1
            bCount.append((i, j, cnt))

    for cx, cy, cnt in bCount:
        board[cx][cy] = max(0, board[cx][cy] - cnt)

    bingCount = checkCount()
    if bingCount >= 2:
        print(answer)
        break
    elif bingCount == 0:
        print(0)
        break