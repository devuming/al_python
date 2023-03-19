import sys
n, l = map(int, sys.stdin.readline().rstrip().split())
pos = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    pos.append((a, b))

pos.sort()
lastIdx = 0 # 널빤지 놓은 마지막 위치
answer = 0

for start, end in pos:
    lastIdx = max(start, lastIdx)
    diff = end - lastIdx
    count = (diff + l - 1) // l
    answer += count
    lastIdx += count * l

print(answer)