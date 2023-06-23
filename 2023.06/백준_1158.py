import sys
from collections import deque
n, k = map(int, sys.stdin.readline().rstrip().split())
result = []
nums = deque([i for i in range(1, n + 1)])

while nums:
    for _ in range(k - 1):
        nums.append(nums.popleft())
    result.append(nums.popleft())

print('<', end='')
for i in range(n):
    if i == 0:
        print(result[i], end='')
    else:
        print(', ' + str(result[i]), end='')
print('>')
