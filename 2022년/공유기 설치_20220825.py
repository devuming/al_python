# 공유기 설치
# C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램
import sys

n, c = map(int, sys.stdin.readline().rstrip().split())
arr = []

for _ in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))
arr.sort()

start = 1
end = arr[-1] - arr[0]
result = 0

while start <= end:
    mid = (start + end) // 2
    value = arr[0]
    count = 1
    for i in range(1, n):
        if arr[i] >= value + mid:
            value = arr[i]
            count += 1
    
    if count >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
print((start+end)//2)