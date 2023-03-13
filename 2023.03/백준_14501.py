# 백준 퇴사 문제
import sys
n = int(sys.stdin.readline().rstrip())
time = []
profit = []
for _ in range(n):
    t, p = map(int, sys.stdin.readline().rstrip().split())
    time.append(t)
    profit.append(p)

dp = [0] * (n + 1)
answer = 0
for i in range(n - 1, -1, -1):   # 6 ~> 0 까지
    if i + time[i] <= n:    
        dp[i] = max(answer, dp[i + time[i]] + profit[i])
        answer = dp[i]
    else:
        dp[i] = answer
        
print(answer)
