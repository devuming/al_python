import sys
n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
x = list(map(int, sys.stdin.readline().rstrip().split()))
result = 0
pos = 0
left = 0
right = n
while left <= right:
    mid = (left + right) // 2
    pos = 0

    for i in x:
        if i - mid <= pos:
            pos = i + mid
        else:
            break
    if pos < n:
        left = mid + 1
    else: 
        right = mid - 1

print(left)