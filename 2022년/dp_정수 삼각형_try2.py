# dp 정수 삼각형
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

dp = [[0] * n for _ in range(n)]
dp[0][0] = arr[0][0]
for i in range(1, n):
    for j in range(len(arr[i])):
        left = 0
        right = dp[i - 1][j]

        if j > 0:
            left = dp[i - 1][j - 1]
        
        dp[i][j] = arr[i][j] + max(left, right)

print(dp)
print(max(dp[n - 1]))