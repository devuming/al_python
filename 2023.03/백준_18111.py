# 백준 18111_마인크래프트
import sys
n, m, b = map(int, sys.stdin.readline().rstrip().split())
boards = []

for _ in range(n):
    board = list(map(int, sys.stdin.readline().rstrip().split()))
    boards.append(board)

ans_time = int(10e9)      # 걸리는 시간
height = 0      # 땅의 높이

for i in range(257):
    use = 0     # 사용한 블록
    take = 0    # 인벤토리에 넣을 블록

    for j in range(n):
        for k in range(m):
            if i > boards[j][k]: # 블록위에 넣기
                use += i - boards[j][k]
            elif i < boards[j][k]:   # 인벤토리에 넣기
                take += boards[j][k] - i

    if use > take + b:
        continue
    time = (use + 2 * take)
    if time <= ans_time:
        ans_time = time
        height = i

print(ans_time, height)