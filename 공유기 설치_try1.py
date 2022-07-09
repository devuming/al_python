# 공유기 설치
n, c = map(int, input().split())
position = []
for _ in range(n):
    position.append(int(input()))

position.sort()     # 이진 탐색을 위한 정렬 수행

start = position[1] - position [0]
end = position[-1] - position[0]
result = 0

while start <= end:
    mid = (start + end) // 2        # 두 공유기 사이의 gap
    value = position[0]
    count = 1
    
    # 현재의 mid 값을 이용해 공유기를 설치
    for i in range(1, n):
        if position[i] >= value + mid:
            value = position[i]
            count += 1
    if count >= c : # c개 이상의 공유기를 설치 할 수 있는 경우, 거리를 증가
        start = mid + 1
        result = mid        # 최적의 결과를 저장
    else:       # c 개 이상의 공유기를 설치할 수 없는 경우, 거리를 감소
        end = mid -1

print(result)