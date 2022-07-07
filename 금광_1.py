# n * m 크기의 금광
# m 번에 걸쳐 오른쪽 위, 오른쪽, 오른쪽 아래 중 하나의 위치로 이동했을때
# 최종적으로 채굴자가 얻을 수 있는 금의 최대 크기
# 첫번째 열부터 시작
# (i, j)는 왼쪽 위, 왼쪽, 왼쪽 아래에서 올 수 있음
# 점화식 a[i][j] = a[i][j] + max(a[i-1][j-1], a[i][j-1], a[i+1][j-1])
import copy
def solution(gold):
    n = len(gold)
    m = len(gold[0])

    dp = copy.deepcopy(gold)

    for i in range(n):
        for j in range(1, m):
            left_top = 0
            left = dp[i][j-1]
            left_bottom = 0
            if i - 1 >= 0:
                left_top = dp[i-1][j-1]
            if i + 1 < n:
                left_bottom = dp[i+1][j-1]

            dp[i][j] = dp[i][j] + max(left_top, left, left_bottom)
    return max([dp[i][m-1] for i in range(n)])

print(solution([[1, 3, 3, 2],[2, 1, 4, 1], [0, 6, 4, 7]]))
print(solution([[1, 3, 1, 5],[2, 2, 4, 1], [5, 0, 2, 3], [0, 6, 1, 2]]))