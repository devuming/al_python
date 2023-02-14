# 큐 구현
import sys
from collections import deque
queue = deque()
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    comm = sys.stdin.readline().rstrip().split()
    if comm[0] == 'push':
        queue.append(comm[1])
    if comm[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
            queue.popleft()
    elif comm[0] == 'size':
        print(len(queue))
    elif comm[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif comm[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif comm[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])