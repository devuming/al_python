import sys
n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().rstrip().split()))
b = list(map(int, sys.stdin.readline().rstrip().split()))
a.sort()
answer = 0
for i in range(n):
    answer += a[i] * max(b)
    b.pop(b.index(max(b)))
print(answer)