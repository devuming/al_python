# 백준 11659_구간합구하기4
# 수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그
import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
sums = [0] * (n + 1)
for i in range(n):
    sums[i + 1] = sums[i] + nums[i]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    print(sums[j] - sums[i - 1])