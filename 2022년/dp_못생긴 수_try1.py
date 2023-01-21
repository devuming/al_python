# dp_못생긴 수
# 못생긴 수 = 2, 3, 5만을 소인수로 가지는 수 (2, 3, 5를 약수로 가지는 합성수)
# N 번째 못생긴 수를 찾는 프로그램
n = int(input())

i2, i3, i5 = 0, 0, 0
next2, next3, next5 = 2, 3, 5
dp = [0] * n
dp[0] = 1
for i in range(1, n):
    dp[i] = min(next2, next3, next5)
    
    if dp[i] == next2:
        i2 += 1
        next2 = dp[i2] * 2
    if dp[i] == next3:
        i3 += 1
        next3 = dp[i3] * 3
    if dp[i] == next5:
        i5 += 1
        next5 = dp[i5] * 5
        
print(dp[n - 1])