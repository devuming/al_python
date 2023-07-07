import sys
import bisect
n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().rstrip().split()))
dp = [a[0]]
index = [0] * n

for i in range(1, n):
    if dp[-1] < a[i]:
        dp.append(a[i])
        index[i] = len(dp) - 1
    else:
        idx = bisect.bisect_left(dp, a[i])
        dp[idx] = a[i]
        index[i] = idx

lis = []
k = len(dp) - 1
for i in range(n - 1, -1, -1):
    if index[i] == k:
        lis.append(a[i])
        k -= 1
    if k == -1:
        break

lis.reverse()
print(len(lis))
print(' '.join(map(str, lis)))
