import sys
from collections import deque
n, m = map(int, sys.stdin.readline().rstrip().split())
ladder = {}
snake = {}

for _ in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    ladder[a] = b
for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    snake[a] = b

visited = [0] * 101
queue = deque()
queue.append(1)

while queue:
    now = queue.popleft()
    # 1 ~ 6 칸 이동
    for i in range(1, 7):
        pos_move = now + i    # 이동 위치
        if pos_move > 100:
            break
        if ladder.get(pos_move):
            pos_move = ladder[pos_move]    # 사다리 타고 이동한 위치
        elif snake.get(pos_move):
            pos_move = snake[pos_move]
        
        if visited[pos_move]:   # 이미 방문한 경우 skip
            continue

        queue.append(pos_move)
        visited[pos_move] = visited[now] + 1

print(visited[100])