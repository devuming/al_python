import sys
from collections import deque

left = deque(list(sys.stdin.readline().rstrip()))
word = deque([])
n = len(left)
m = int(sys.stdin.readline().rstrip())

for _ in range(m):
    comm = sys.stdin.readline().rstrip().split()
    if comm[0] == 'L':
        if len(left) > 0:      # 맨앞이 아닌 경우
            word.appendleft(left.pop())
    elif comm[0] == 'D':
        if len(word) > 0:  # 맨뒤가 아닌 경우
            left.append(word.popleft())
    elif comm[0] == 'B':
        if len(left) > 0:
            left.pop()
    else:
        left.append(comm[1])
    print(left, word)
print(''.join(left) + ''.join(word))
