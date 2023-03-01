import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
woods = list(map(int, sys.stdin.readline().rstrip().split()))

left = 0
right = sum(woods)

while left <= right:
    mid = (left + right) // 2
    total = 0

    for w in woods:
        if w > mid:
            total += w - mid

    if total < m:
        right = mid - 1
    else:
        left = mid + 1

print(right)