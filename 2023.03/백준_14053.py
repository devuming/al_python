import sys
from collections import deque
# 반시계 방향 90도 상->좌 좌->하 하->우 우->상
dirs = {0: (-1, 0), 1:(0, 1), 2:(1, 0), 3:(0, -1)}   # 상우하좌 (시계방향)
# 방향 - 1: 0>3>2>1
# 0 - 1 = 상 -> 좌 = -1 (3)
# 3 - 1 = 좌 -> 하 = 2
# 2 - 1 = 하2 ->우1 = 1
# 1 - 1 = 우1 -> 상0
cnt = 0
def dfs(r, c, d):
    global cnt
    if board[r][c] == 0:
       board[r][c] = 2
       cnt += 1

    # 주변 4칸 확인
    for i in range(4):
        nd = (d + 3 - i) % 4
        x = r + dirs[nd][0]
        y = c + dirs[nd][1]
        if x < 0 or x >= n or y < 0 or y >= m:
            continue            
        if board[x][y] == 0:    # 청소되지 않은 경우
            dfs(x, y, nd)

    # 후진
    nx = r - dirs[d][0]
    ny = c - dirs[d][1]

    if board[nx][ny] == 1:
        print(cnt)
        exit(0)
    dfs(nx, ny, d)

n, m = map(int, sys.stdin.readline().rstrip().split())
r, c, d = map(int, sys.stdin.readline().rstrip().split())
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))
dfs(r, c, d)

for b in board:
    print(b)