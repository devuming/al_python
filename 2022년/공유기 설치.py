# 공유기 설치
# 집 N 개가 수직선 위에 있음
# 공유기 C 개를 설치하려고 함
# 한 집엔 공유기 하나만 설치가능, 공유기 거리를 가능한 크게 하여 설치
# 출력 : 가장 인접한 두 공유기 사이의 최대거리

# 집, 공유기 개수 입력
n, c = map(int, input().split())
array = []

for _ in range(n):
    array.append(int(input()))  # 2 <= N <= 200,000
array.sort()        # 정렬

# 집의 좌표를 나타냄
start = array[0]
end = array[len(array) - 1]     # 제일 마지막 집
result = 0

while start <= end:
    mid = (start + end) // 2
    value = array[0]
    count = 1   # 설치된 공유기 갯수

    # mid 값으로 공유기 설치
    for i in range(1, n):
        if array[i] >= value + mid:     # mid에 공유기 설치했을때 거리보다 array[i] 의 위치가 더 큰 경우 
            value = array[i]            # 설치 위치 조정
            count += 1

    if count >= c:          # 공유기 위치
        start = mid + 1
        result = mid    # 최적의 결과 저장
    else :                  # C 개 이상 설치할 수 없는 경우 거리 감소
        end = mid - 1
        
print(result)