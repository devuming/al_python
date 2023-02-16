# 수 찾기
# n개의 정수가 주어져있을 때, X 라는 정수가 존재하는지 알아내는 프로그램
import sys
from collections import Counter
n = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
cnt_nums = Counter(nums)
m = int(sys.stdin.readline().rstrip())
x_nums = list(map(int, sys.stdin.readline().rstrip().split()))

for i in range(m):
    if cnt_nums.get(x_nums[i], 0) > 0:
        print(1)
    else:
        print(0)