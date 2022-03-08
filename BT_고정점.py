# 고정점
# 인덱스와 저장된 원소가 값이 같으면 고정점
# 원소가 오름차순으로 정렬되어있을 때 고정점을 출력
# 없을 경우 -1 

def searchFixPoint(array) : 
    start = 0
    end = len(array) - 1
    mid = (start + end) // 2

    while start <= end :
        if array[mid] == mid:
            return mid
        elif array[mid] < mid:          # 원소값이 인덱스 값보다 작은 경우 오른쪽 탐색 (큰 값)
            start = mid + 1
            mid = (start + end) // 2
        elif array[mid] > mid:          # 원소값이 인덱스 값보다 큰 경우 왼쪽 탐색 (작은 값)
            end = mid - 1
            mid = (start + end) // 2

    return None

n = int(input())
array = list(map(int, input().split()))

fixPoint = searchFixPoint(array)

if fixPoint == None : 
    print('-1')
else:
    print(fixPoint)