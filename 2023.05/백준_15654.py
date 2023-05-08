import sys
from itertools import permutations
n, m = map(int, sys.stdin.readline().rstrip().split())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
perm = list(permutations(nums, m))
perm.sort()
for p in perm:
    print(' '.join(list(map(str, p))))