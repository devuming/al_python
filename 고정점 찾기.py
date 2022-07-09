# 고정점 찾기
# 정렬된 리스트가 주어질 때, 값이 인덱스와 동일한 원소
# 시간 복잡도 O(logN)
n = int(input())
nums = list(map(int, input().split()))

start = 0
end = len(nums)-1
mid = (start + end) // 2
result = -1

while start <= end:
    mid = (start + end) // 2

    if nums[mid] < mid:
        start = mid + 1
    elif nums[mid] > mid:
        end = mid - 1

    elif nums[mid] == mid:        # 고정점
        result = mid
        break

print(result)
        