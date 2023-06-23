def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)


n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

step = nums[1] - nums[0]
for i in range(2, n):
    step = gcd(step, nums[i] - nums[i-1])

cnt = 0
for i in range(n - 1):
    cnt += (nums[i + 1] - nums[i]) // step - 1
print(cnt)
