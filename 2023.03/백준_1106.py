import sys
c, n = map(int, sys.stdin.readline().rstrip().split())
dp = [10e9] * (c + 100)
dp[0] = 0
costs = []
for _ in range(n):
    cost, cnt = map(int, sys.stdin.readline().rstrip().split())
    costs.append((cost, cnt))

for cost, cnt in costs:
    for i in range(cnt, c + 100):
        dp[i] = min(dp[i], dp[i - cnt] + cost)
print(min(dp[c:]))