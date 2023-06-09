import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
balls = [i for i in range(1, n + 1)]
for _ in range(m):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    balls[i - 1], balls[j - 1] = balls[j - 1], balls[i - 1]

print(' '.join(list(map(str, balls))))