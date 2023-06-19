import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
nums = list(set(map(int, sys.stdin.readline().rstrip().split())))
nums.sort()


def dfs(arr, cnt, idx):
    global n, m
    if cnt == m:
        print(' '.join(map(str, arr)))
        return
    for i in range(idx, len(nums)):
        arr.append(nums[i])
        dfs(arr, cnt + 1, i)
        arr.pop()


dfs([], 0, 0)
