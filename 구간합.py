# 구간합_백준 : 구간 합 구하기 4
import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
d = [0] * (n + 1)

for i in range(1, n + 1):
    d[i] = d[i - 1] + arr[i - 1]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().rstrip().split())

    print(d[j] - d[i - 1])
