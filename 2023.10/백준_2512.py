# 예산 상한액
import sys
n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
total = int(sys.stdin.readline().rstrip())
left = 0
right = max(arr)
answer = 0
while left <= right:
    mid = (left + right) // 2
    budget = 0

    for a in arr:
        if a > mid:
            budget += mid
        else:
            budget += a

    if budget < total:
        left = mid + 1
        answer = mid
    elif budget > total:
        right = mid - 1
    else:
        answer = mid
        break
print(answer)
