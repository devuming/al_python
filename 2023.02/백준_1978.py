# 백준 1978_소수 찾기
# N개 중에서 소수가 몇 개인지 찾아서 출력
import sys, math
n = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().rstrip().split()))

count = 0
for num in nums:
    if num <= 1:
        continue
    count += 1
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            count -= 1
            break

print(count)