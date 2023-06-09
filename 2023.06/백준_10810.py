import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
balls = [0] * n
for _ in range(m):
    i, j, k = map(int, sys.stdin.readline().rstrip().split())

    for b in range(i - 1, j):
        balls[b] = k
print(' '.join(list(map(str, balls))))