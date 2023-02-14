# 덱
import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())
deq = deque()
for _ in range(n):
    comm = sys.stdin.readline().rstrip()
    if comm == 'pop_front':
        if len(deq) == 0:
            print(-1)
        else:
            x = deq.popleft()
            print(x)
    elif comm == 'pop_back':
        if len(deq) == 0:
            print(-1)
        else:
            x = deq.pop()
            print(x)
    elif comm == 'size':
        print(len(deq))
    elif comm == 'empty':
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    elif comm == 'front':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[0])
    elif comm == 'back':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[-1])
    else:
        comm, num = comm.split()
        if comm == 'push_front':
            deq.appendleft(num)
        elif comm == 'push_back':
            deq.append(num)