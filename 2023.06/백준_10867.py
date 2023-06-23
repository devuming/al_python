import sys
n = int(sys.stdin.readline().rstrip())
nums = list(set(map(int, sys.stdin.readline().rstrip().split())))
nums.sort()
print(' '.join(map(str, nums)))
