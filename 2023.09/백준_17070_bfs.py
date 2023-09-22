import sys
sys.setrecursionlimit(2500)

n = int(sys.stdin.readline().rstrip())
board = []

for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))


def dfs(x1, y1, x2, y2):
    global n

    if (x2, y2) == (n - 1, n - 1):
        return 1

    count = 0

    # 현재 가로|대각선인 경우
    if y1 != y2:
        # 가로 이동
        if y2 + 1 < n and board[x2][y2 + 1] == 0:
            count += dfs(x2, y2, x2, y2 + 1)

    # 현재 세로|대각선인 경우
    if x1 != x2:
        # 세로 이동
        if x2 + 1 < n and board[x2 + 1][y2] == 0:
            count += dfs(x2, y2, x2 + 1, y2)

    # 대각선 이동
    if (x2 + 1 < n and y2 + 1 < n
            and (board[x2][y2 + 1], board[x2 + 1][y2], board[x2 + 1][y2 + 1]) == (0, 0, 0)):
        count += dfs(x2, y2, x2 + 1, y2 + 1)

    return count


print(dfs(0, 0, 0, 1))
