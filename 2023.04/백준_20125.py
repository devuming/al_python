import sys
from collections import deque
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
queue = deque()

n = int(sys.stdin.readline().rstrip())
board = []
for _ in range(n):
    board.append(list(sys.stdin.readline().rstrip()))

hx, hy = (-1, -1)
for i in range(n):
    for j in range(n):
        if board[i][j] != '*':
            continue
        isHeart = 0 # 사방이 * 이면 심장
        for dx, dy in dirs:
            nx = i + dx
            ny = j + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if board[nx][ny] == '*':
                isHeart += 1

        if isHeart == 4:
            hx, hy = (i, j)
            break
    if (hx, hy) != (-1, -1):
        break
    
d_cnt = [0, 0, 0, 0, 0] # 오_팔, 왼_팔, 오_다리, 왼_다리, 허리

d_cnt[0] = hy - board[hx].index('*') #오_팔
for i in range(hy + 1, n):
    if i == n - 1:
        d_cnt[1] = i - hy
    if board[hx][i] == '_':
        d_cnt[1] = (i - 1) - hy  #왼_팔
        break
# 허리
nx = 0
for i in range(hx + 1, n):
    if board[i][hy] == '_':
        d_cnt[2] = (i - 1) - hx
        nx = i
        break

for i in range(nx, n):
    if i == n - 1:
        d_cnt[3] = n - nx
    if board[i][hy - 1] == '_': # 왼다리
        d_cnt[3] = i - nx
        break

for i in range(nx, n):
    if i == n - 1:
        d_cnt[4] = n - nx
    if board[i][hy + 1] == '_': # 오른다리
        d_cnt[4] = i - nx
        break

print(hx + 1, hy + 1)
print(' '.join(list(map(str, d_cnt))))