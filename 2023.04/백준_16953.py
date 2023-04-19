# A -> B
# 2를 곱하거나/1을 수의 가장 오른쪽에 추가하거나
import sys
from collections import deque
a, b = map(int, sys.stdin.readline().rstrip().split())
queue = deque()
queue.append((a, 1))
answer = -1
while queue:
    now, cnt = queue.popleft()
    if now == b:
        answer = cnt
        break
    n1 = int(str(now) + '1')
    n2 = now * 2

    if n1 <= b:
        queue.append((n1, cnt + 1))
    if n2 <= b:
        queue.append((n2, cnt + 1))

print(answer)