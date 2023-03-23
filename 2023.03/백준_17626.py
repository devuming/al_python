import sys, math

n = int(sys.stdin.readline().rstrip())
dp = [0, 1]
nums = [[0], [1]]
for i in range(2, n + 1):
    min_value = 10e8
    for j in range(1, int(math.sqrt(i)) + 1):
        min_value = min(min_value, dp[i - j ** 2])
    dp.append(min_value + 1)

print(dp[n])