# 정렬된 배열에서 특정수의 개수 구하기
from bisect import bisect_left, bisect_right

def value_count(nums, x):
    count = bisect_right(nums, x) - bisect_left(nums, x)
    return count if count > 0 else -1

n, x = map(int, input().split())
nums = list(map(int, input().split()))
print(value_count(nums, x))

