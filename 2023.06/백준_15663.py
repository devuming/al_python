import sys
from itertools import permutations
n, m = map(int, sys.stdin.readline().rstrip().split())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
answer = set(permutations(nums, m))
answer = sorted(answer)

for ans in answer:
    print(' '.join(list(map(str, ans))))