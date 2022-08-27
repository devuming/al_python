# dp_LIS (가장 긴 증가하는 부분순열)
# 이중 for 문 solution
arr = list(map(int, input().split()))
n = len(arr)
dp = [1] * n

for i in range(n):
    for j in range(0, i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(dp)
print(max(dp))