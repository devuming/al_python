import sys
import bisect
n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().rstrip().split()))
lis = [a[0]]
for i in range(1, n):
    if lis[-1] < a[i]:
        lis.append(a[i])
    else:
        idx = bisect.bisect_left(lis, a[i])
        lis[idx] = a[i]
print(len(lis))
