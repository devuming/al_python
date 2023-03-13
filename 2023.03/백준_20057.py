import sys, math
n = int(sys.stdin.readline().rstrip())
boards = [[0] * (n + 2) for _ in range(n + 2)]

for i in range(n):
    board = list(map(int, sys.stdin.readline().rstrip().split()))
    for j, b in enumerate(board):
        boards[i + 1][j + 1] = b

dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]   # 좌-하-우-상 (토네이도 이동방향)
cnt = 1
x, y = math.ceil(n / 2), math.ceil(n / 2)

while cnt < n:
    for i, dir in enumerate(dirs):
        if i == 2:   # 오른방향 면 이동 칸 갯수 증가
            cnt += 1
        print(x, y, cnt)
        x = x + (dir[0] * cnt)
        y = y + (dir[1] * cnt)

        # 주변 모래 처리
    cnt += 1
    
print(boards[0][0])