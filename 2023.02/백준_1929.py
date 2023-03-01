# 백준 1929 소수 구하기 M이상 N 이하의 소수 모두 출력
import sys, math
def isPrime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False    # 소수가 아님
    return True
    
m, n = map(int, sys.stdin.readline().rstrip().split())
nums = [True] * (n - m + 1)

for num in range(m, n + 1):
    if num < 2:
        nums[num - m] = False
    if not nums[num - m]:
        continue
    if isPrime(num):
        # 소수일 경우, 소수의 배수는 소수가 아니므로 False 처리
        k = 2
        while (num * k) <= n:
            nums[(num * k) - m] = False
            k += 1
    else:
        # 소수가 아닌 경우
        nums[num - m] = False

# 소수 출력
for i, num in enumerate(nums):
    if num:
        print(i + m)