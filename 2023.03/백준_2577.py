import sys
from collections import Counter
a = int(sys.stdin.readline().rstrip())
b = int(sys.stdin.readline().rstrip())
c = int(sys.stdin.readline().rstrip())

cnt = Counter(str(a * b * c))   # str은 iterable

for i in range(0, 10):
    print(cnt.get(str(i), 0))