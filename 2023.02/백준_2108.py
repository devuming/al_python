# 백준 2108_통계학
import sys
from collections import Counter

n = int(sys.stdin.readline().rstrip())
nums = []

for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    nums.append(num)
nums.sort()

# 산술 평균
print(round(sum(nums) / len(nums)))
# 중앙 값
print(nums[len(nums) // 2])
# 최빈값
dic_nums = Counter(nums).most_common()
if len(dic_nums) > 1 and dic_nums[0][1] == dic_nums[1][1]: # 여러개일 경우, 최빈값중 두번째로 작은값
    print(dic_nums[1][0])
else:
    print(dic_nums[0][0])
# 범위
print(max(nums) - min(nums))