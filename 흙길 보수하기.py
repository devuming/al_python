# 흙길 보수하기
# N개의 물웅덩이를 길이 L의 널빤지로 물웅덩이를 덮으려 할 때, 널빤지들의 최소갯수
import sys
n, l = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))    # 물웅덩이의 위치정보 저장

arr.sort(key = lambda x:x[0])
count = 0 
start = 0
for s, e in arr:
    if s > start:
        start = s

    while start < e:
        start += l
        count += 1

print(count)