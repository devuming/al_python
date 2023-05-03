from collections import deque
n = int(input())
board = []
max_height = 0
for _ in range(n):
    b = list(map(int, input().split()))
    board.append(b)
    max_height = max(max(b), max_height)

def bfs(i, j, visited, height):
    queue = deque([(i, j)])
    visited[i][j] = True
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    cnt = 0
    while queue:
        x, y = queue.popleft()
        cnt += 1

        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny]:
                    continue
                if board[nx][ny] <= height:
                    continue
                visited[nx][ny] = True
                queue.append((nx, ny))
    return cnt

h = 0
answer = 0
while h <= max_height:
    visited = [[False] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and board[i][j] > h:
                bfs(i, j, visited, h)
                cnt += 1
    answer = max(answer, cnt)
    h += 1
print(answer)