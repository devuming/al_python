import sys
n, k = map(int, sys.stdin.readline().rstrip().split())
values = [(0, 0)]
for _ in range(n):
    weight, value = map(int, sys.stdin.readline().rstrip().split())
    values.append((weight, value))

dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        weight = values[i][0]
        value = values[i][1]
        if j < weight:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(value + dp[i - 1][j - weight], dp[i - 1][j])

print(dp[n][k])
