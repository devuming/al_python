import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
balls = [i for i in range(1, n + 1)]
for _ in range(m):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    temp = balls[i-1:j]
    for b in range(i, j+1):
        balls[b-1] = temp[-1]
        temp.pop()

print(' '.join(list(map(str, balls))))