import sys
from itertools import combinations
t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    clothes = {}
    for _ in range(n):
        cloth, kind = sys.stdin.readline().rstrip().split()
        if clothes.get(kind) is None:
            clothes[kind] = []
        clothes[kind].append(cloth)

    count = 1
    combi = 1
    for key in clothes.keys():
        count *= len(clothes[key]) + 1
    print(count - 1)
    