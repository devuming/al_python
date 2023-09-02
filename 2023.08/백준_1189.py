import sys
r, c, k = map(int, sys.stdin.readline().rstrip().split())
board = []
for _ in range(r):
    board.append(sys.stdin.readline().rstrip())


def dfs(visited, x, y, dist):
    global r, c, k
    count = 0
    if (x, y) == (0, c - 1):
        if dist == k:
            return 1
        else:
            return 0

    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in dirs:
        nx = x + dx
        ny = y + dy

        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            continue
        if visited[nx][ny] or board[nx][ny] == 'T':
            continue
        visited[nx][ny] = True
        count += dfs(visited, nx, ny, dist + 1)
        visited[nx][ny] = False

    return count


visited = [[False] * c for _ in range(r)]
visited[r - 1][0] = True
print(dfs(visited, r-1, 0, 1))
