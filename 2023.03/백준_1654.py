import sys
k, n = map(int, sys.stdin.readline().rstrip().split())

nums = []
for _ in range(k):
    num = int(sys.stdin.readline().rstrip())
    nums.append(num)

start = 1
end = max(nums)

while start <= end:
    mid = (start + end) // 2
    count = 0
    for num in nums:
        count += num // mid

    if count < n:
        end = mid - 1
    else:
        start = mid + 1

print(end)