# 프린터 큐
import sys
from collections import deque
t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    queue = deque(list(map(int, sys.stdin.readline().rstrip().split())))
    
    count = 0
    while queue:
        first = max(queue)
        front = queue.popleft()
        m -= 1
        if first == front:
            count += 1
            if m < 0:
                print(count)
                break
        else:
            queue.append(front)
            if m < 0:
                m = len(queue) - 1