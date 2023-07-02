import sys
n = int(sys.stdin.readline().rstrip())
chains = list(map(int, sys.stdin.readline().rstrip().split()))
chains.sort(reverse=True)

count = 0
while n > 0 and chains:
    now = chains.pop()
    print(n, now, count)
    if n - 1 >= now:
        n -= now + 2
        count += now
    else:
        count += n - 1
        break
print(count)
