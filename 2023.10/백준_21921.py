import sys
n, x = map(int, sys.stdin.readline().rstrip().split())
visitors = list(map(int, sys.stdin.readline().rstrip().split()))

total = sum(visitors[0:x])
max_total = total
answer = 1

for i in range(x, n):
    total += visitors[i]
    total -= visitors[i - x]

    if max_total < total:
        max_total = total
        answer = 1
    elif max_total == total:
        answer += 1

if max_total == 0:
    print("SAD")
else:
    print(max_total)
    print(answer)
