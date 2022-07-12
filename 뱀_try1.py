# 뱀
from collections import deque

n = int(input())    # 보드 크기 좌표
k = int(input())    
matrix = [[0] * (n + 1) for _ in range(n + 1)]        # 0 : 아무것도 없음, 1: 뱀, -1 : 사과

for _ in range(k):
    x, y = map(int, input().split())
    matrix[x][y] = -1           # 사과 위치 표시

l = int(input())
dir = deque()               # 방향 전환 정보
for _ in range(l):
    x, c = input().split()
    dir.append((int(x), c))   # 초, 방향

second = 0 

nx = 1
ny = 1
now_dir = (0, 1)    # 초기 우측 이동
snakes = deque()
snakes.append((nx, ny))
snake_length = 1    # 초기 뱀 길이

while True:   
    if dir and dir[0][0] == second:
        x, c = dir.popleft()
        now_x, now_y = now_dir

        # 방향 변경
        if now_x == 0:
            now_dir = (now_y, now_x) if c == 'D' else (-now_y, now_x)
        elif now_y == 0:
            now_dir = (now_y, now_x) if c == 'L' else (now_y, -now_x)

    # 방향에 따라 좌표 이동
    nx += now_dir[0]
    ny += now_dir[1]    
    second += 1         # 이동 후 초 증가
    
    if nx == 0 or ny == 0 or nx > n or ny > n or matrix[nx][ny] == 1: # 이동할 위치가 벽을 만나거나 자신의 몸과 부딪히는 경우
        break
    
    if matrix[nx][ny] == 0:    # 사과가 없는 경우
        # 꼬리 위치 이동 (몸길이 그대로)
        a, b = snakes.popleft()
        matrix[a][b] = 0

    # 뱀 이동
    matrix[nx][ny] = 1  # 몸 표시
    snakes.append((nx, ny))    

print(second)