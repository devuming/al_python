# 소수 - M~N 까지의 자연수 중 소수인 것을 모두 골라 소수의 합과 최소값을 찾는 프로그램
import sys, math
m = int(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline().rstrip())

nums = [True] * (n - m + 1)    # m ~ n 까지 (True : 소수, False : 소수 아님)
total = 0
min_value = 10001

def isPrime(num):   # num이 소수인지 판별하는 함수
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
    
for i in range(len(nums)):
    if not nums[i]:
        continue
    if m + i == 1:
        nums[i] = False
        continue
    if isPrime(m + i):
        total += m + i
        k = 2
        # 소수의 배수 제거
        while (m + i) * k <= n:
            num = (m + i) * k
            nums[num - m] = False
            k += 1
    else:
        nums[i] = False # 소수 아님

for i in range(len(nums)):
    if nums[i] and (m + i) < min_value:
        min_value = m + i

if total == 0:
    print(-1)
else:
    print(total)
    print(min_value)
