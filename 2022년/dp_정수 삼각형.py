# 정수 삼각형
# 맨 위층 부터 시작해서 아래에 있는 수 중 하나를 선택해 아래층으로 내려올 때
# 수의 합이 최대가 되는 경로를 구하는 프로그램
# 현재 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것중에서만 선택 가능
# 입력 : 삼각형의 크기 n, 정수 삼각형
# 출력 : 합이 최대가 되는 경로에 있는 수의 합 출력
from numpy import array


n = int(input())
dp = []

for _ in range(n):
    array = list(map(int, input().split()))
    dp.append(array)

for i in range(n):
    for j in range(i + 1):

        if j == 0:
            left = 0
        else:
            left = dp[i - 1][j-1]

        if i == j :
            right = 0
        else:
            right =  dp[i - 1][j]

        dp[i][j] = dp[i][j] + max(left, right)      # 대각선 왼쪽, 오른쪽 더한 것 중 큰거

print(dp)

# 최대값 출력
print(max(dp[n-1]))