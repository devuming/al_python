# 백준 10986 나머지 합
import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
sums = [0] * (n + 1)
count = [0] * m     # m 으로 나눈 나머지 별 구간합 갯수

# sums[i] % M == sum[j] % M 인 구간합 갯수
for i in range(1, n + 1):
    sums[i] = (sums[i - 1] + nums[i - 1]) % m
    count[sums[i]] += 1 # 나머지가 같은 구간합 갯수 증가 

result = count[0]   # i == j 일 때, 나머지가 0인 구간합길이=1 갯수

for i in range(m):
    if count[i] < 2:    # 나머지가 같은 구간합이 2개 이상일 경우에만
        continue
    result += count[i] * (count[i] - 1) // 2       # 나머지 같은 구간합 중 2개를 고르는 경우의 수 계산

print(result) 