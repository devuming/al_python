# 요세푸스 문제 0
import sys
from collections import deque

n, k = map(int, sys.stdin.readline().rstrip().split())

nums = [i for i in range(1, n + 1)]
queue = deque([i for i in range(1, n + 1)])

print('<', end='')
while queue:
    for i in range(k - 1):
        queue.append(queue[0])
        queue.popleft()
    print(queue.popleft(), end='')

    if queue:
        print(', ', end="")
print(">")