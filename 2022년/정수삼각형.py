# 정수 삼각형
# 맨 위층에서 시작하여 아래로 내려올때 선택된 값의 합이 최대가 되는 경로를 구하는 프로그램
# 대각선 왼쪽/대각선 오른쪽의 것만 선택 가능
# 점화식 : dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])
import copy

def solution(tri):
    n = len(tri)
    answer = 0      # 최댓값
    dp = copy.deepcopy(tri)

    for i in range(1, n):
        for j in range(len(tri[i])):
            if j - 1 > -1:          # 대각선 왼쪽 위
                left = dp[i-1][j-1]
            else:
                left = 0

            if j < len(tri[i-1]):   # 대각선 오른쪽 위
                right = dp[i-1][j]
            else:
                right = 0

            dp[i][j] = dp[i][j] + max(left, right)      # 대각선 왼쪽 위/오른쪽 위 둘 중 무엇과 더하는 것이 최대값인지
    
    return max(dp[n - 1])

print(solution([[7],[3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))