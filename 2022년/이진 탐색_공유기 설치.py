# 이진 탐색_공유기 설치
# C개의 공유기를 N개의 집에 설치하여, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램
import sys
n, c = map(int, input().split(' ')) 
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))

arr.sort()      # 집 좌표 순 정렬

result = 0
min_gap = arr[1] - arr[0]       # 가장 공유기 사이의 거리가 가까운 경우
max_gap = arr[-1] - arr[0]      # 가장 공유기 사잉의 거리가 먼 경우

while min_gap <= max_gap:    # 이진 탐색
    mid_gap = (min_gap + max_gap) // 2      # 거리의 중간 값
    loc = arr[0]    # 공유기 설치 위치
    count = 1       # 공유기 설치 갯수

    # 공유기 설치하기 
    for i in range(1, n):
        if arr[i] >= loc + mid_gap:     # 이전 설치된 위치와 gap 만큼 차이나는 위치에 공유기 설치
            loc = arr[i]
            count += 1

    if count >= c:
        min_gap = mid_gap + 1   # gap 키우기
        result = mid_gap
    else:  # 원하는 갯수 만큼 공유기 설치를 못한 경우 gap 줄이기
        max_gap = mid_gap - 1


print(result)