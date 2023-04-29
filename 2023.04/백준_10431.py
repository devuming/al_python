import sys
p = int(sys.stdin.readline().rstrip())
answer = []
for _ in range(p):
    nums = list(map(int, sys.stdin.readline().rstrip().split()))
    t = nums[0]
    nums = nums[1:]
    cnt = 0
    for i, num in enumerate(nums):
        for j in range(0, i):
            if num < nums[j]:
                cnt += 1

    answer.append(cnt)

for i, ans in enumerate(answer):
    print(i + 1, ans)