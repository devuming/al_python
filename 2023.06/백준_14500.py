import sys
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
answer = 0


def dfs(i, j, step, total):
    global answer
    if total + max_val * (4 - step) <= answer:
        return
    if step == 4:
        answer = max(answer, total)
        return
    for dx, dy in dir:
        nx = i + dx
        ny = j + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if visited[nx][ny]:
            continue
        if step == 2:
            # 두번째 블록 다음은 기존 좌표에서 탐색 재개 (ㅏ, ㅓ, ㅗ, ㅜ)
            visited[nx][ny] = True
            dfs(i, j, step + 1, total + board[nx][ny])
            visited[nx][ny] = False
        visited[nx][ny] = True
        dfs(nx, ny, step + 1, total + board[nx][ny])
        visited[nx][ny] = False


n, m = map(int, sys.stdin.readline().rstrip().split())
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))

max_val = max(map(max, board))
visited = [[False] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, 1, board[i][j])
        visited[i][j] = False

print(answer)
