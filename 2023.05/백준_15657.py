import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
nums.sort()

temp = []
def dfs(start):
    if len(temp) == m:
        print(' '.join(list(map(str, temp))))
        return
    for i in range(start, n):
        temp.append(nums[i])
        dfs(i)
        temp.pop()
dfs(0)