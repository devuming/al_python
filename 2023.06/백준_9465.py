import sys
t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    nums = []
    for _ in range(2):
        nums.append(list(map(int, sys.stdin.readline().rstrip().split())))
    if n == 1:
        print(max(nums[0][n - 1], nums[1][n - 1]))
        continue

    nums[0][1] += nums[1][0]
    nums[1][1] += nums[0][0]

    for i in range(2, n):
        nums[0][i] = max(nums[1][i - 1], nums[1][i - 2]) + nums[0][i]
        nums[1][i] = max(nums[0][i - 1], nums[0][i - 2]) + nums[1][i]

    print(max(nums[0][n - 1], nums[1][n - 1]))
