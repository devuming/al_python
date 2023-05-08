import sys
from collections import Counter
t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    w = sys.stdin.readline().rstrip()
    k = int(sys.stdin.readline().rstrip())
    cnt = Counter(w)
    print(cnt)
    answer = 10e9
    for key, value in cnt.items():
        if value == k:
            temp = (len(w) - w[::-1].index(key) - 1) - w.index(key) + 1
            print(key)
            print(w.index(key), len(w) - w[::-1].index(key) -1)
            answer = min(answer, temp)
            print(temp)
    print(answer)