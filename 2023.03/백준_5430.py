import sys
from collections import deque
t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline().rstrip())
    nums = sys.stdin.readline().rstrip()[1:-1]
    if len(nums) > 0:
        nums = deque(nums.split(','))
    else:
        nums = deque()

    if p.count('D') > len(nums):
        print("error")
        continue

    r_flag = False
    for func in p:
        if func == 'R':
            r_flag = not r_flag
        elif func == 'D':
            if r_flag:
                nums.pop()
            else:
                nums.popleft()
    if r_flag:
        nums.reverse()

    result = ','.join(nums)
    print(f'[{result}]')