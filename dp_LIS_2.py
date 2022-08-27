# dp_LIS_2
# 이진 탐색
import sys, bisect
arr = list(map(int, sys.stdin.readline().rstrip().split()))
lis = []
lis.append(arr[0])
# 1 3 4 
# 2 -> 1 > 1 2 4
# 
for i in range(1, len(arr)):
    if lis[-1] < arr[i]:
        lis.append(arr[i])
    else:
        idx = bisect.bisect_left(lis, arr[i])
        lis[idx] = arr[i]

print(lis)