import sys
n, k = map(int, sys.stdin.readline().rstrip().split())
values = []
for _ in range(n):
    values.append(tuple(map(int, sys.stdin.readline().rstrip().split())))
values.sort()
dp = [[0] * (k + 1) for _ in range(n)]

for i in range(n):
    for j in range(1, k + 1):
        weight = values[i][0]
        value = values[i][1]
        if j < weight:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(value + dp[i - 1][j - weight], dp[i - 1][j])

print(dp[n - 1][k])