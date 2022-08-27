# dp_병사 배치하기
# 무작위로 나열되어있는 N명의 병사에서 특정 위치의 병사를 열외시켜 내림차순으로 배치할때
# 남아있는 병사의 수가 최대가 되도록 하기 위해서 열외시켜야하는 병사의 수
# LIS 로 풀어보자
# def binary_search(dp, start, end):
#     while True:
#         mid = (start + end) // 2
#         if dp[mid]

import sys
n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split(' ')))
dp = [1] * n
arr.reverse()

for i in range(1, n):
    for j in range(0, i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(dp)
print(n - max(dp))