import sys
from collections import Counter
n = int(sys.stdin.readline().rstrip())
first = sys.stdin.readline().rstrip()
answer = 0

for _ in range(n - 1):
    word = sys.stdin.readline().rstrip()
    cnt = Counter(first)

    if abs(len(word) - len(first)) > 1:
        continue
    diff = 0
    for w in word:
        cnt[w] = cnt.get(w, 0) - 1

    for value in cnt.values():
        diff += abs(value)
    if diff <= 2:
        answer += 1
print(answer)
