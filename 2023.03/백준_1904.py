import sys
n = int(sys.stdin.readline().rstrip())
dp = [0] * (10000001) # [0] * (n + 1) 로 하면 N = 1 인 경우 오류가 발생하게 된다.
dp[1] = 1
dp[2] = 2

for i in range(3, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 15746

print(dp[n])