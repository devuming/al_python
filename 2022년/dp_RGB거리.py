# RGB 거리 _ DP
# N개의 집을 빨강, 초록, 파랑 중 하나의 색으로 칠할 때, 모든 집을 칠하는 비용의 최소값을 구함
# 1번집은 2번집과 색이 같지 않아야함
# N번 집은 N - 1 번 집과 색이 같지 않아야함
# i번 집은 i-1번, i+1번 집과 색이 같지 않아야함
n = int(input())
rgb = [[0, 0, 0]]
for _ in range(n):
    rgb.append(list(map(int, input().split())))

dp = [[0] * (n + 1) for _ in range(3)]  # n개의 집을 칠하는데 드는 비용, R/G/B 채널 별

for i in range(1, n + 1):  
    dp[0][i] = rgb[i][0] + min(dp[1][i - 1], dp[2][i - 1]) # i 번째 집에 R을 칠하는 경우
    dp[1][i] = rgb[i][1] + min(dp[0][i - 1], dp[2][i - 1]) # i 번째 집에 G 를 칠하는 경우     
    dp[2][i] = rgb[i][2] + min(dp[0][i - 1], dp[1][i - 1]) # i 번째 집에 B 를 칠하는 경우 

    for d in dp:
        print(d)
    print('----')

print(min(dp[i][n] for i in range(3)))
