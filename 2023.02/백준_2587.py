# 평균과 중앙값
import sys
nums = []
sum = 0
for _ in range(5):
    num = int(sys.stdin.readline().rstrip())
    sum += num
    nums.append(num)

nums.sort()
print(sum // 5)
print(nums[2])