import sys

n = int(sys.stdin.readline().rstrip())
board = []

for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))

dp = [[[0] * n for _ in range(n)] for _ in range(3)]
dp[0][0][1] = 1
for i in range(2, n):
    if board[0][i] == 0:
        dp[0][0][i] = dp[0][0][i-1]  # 첫째줄 가로이동은 0 뿐

for i in range(1, n):
    for j in range(1, n):
        # 대각선 이동
        if board[i][j] == 0 and board[i - 1][j] == 0 and board[i][j - 1] == 0:
            dp[2][i][j] = dp[0][i - 1][j - 1] + \
                dp[1][i - 1][j - 1] + dp[2][i - 1][j - 1]
        if board[i][j] == 0:
            # 가로 이동
            dp[0][i][j] = dp[0][i][j - 1] + dp[2][i][j - 1]
            # 세로 이동
            dp[1][i][j] = dp[1][i - 1][j] + dp[2][i - 1][j]

print(dp)
print(dp[0][n - 1][n - 1] + dp[1][n - 1][n - 1] + dp[2][n - 1][n - 1])
