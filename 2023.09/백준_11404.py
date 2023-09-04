import sys
n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
cost = [[10e9] * n for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    cost[a - 1][b - 1] = min(cost[a - 1][b - 1], c)

for i in range(n):
    cost[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
for c in cost:
    for j in c:
        if j == 10e9:
            print(0, end=' ')
        else:
            print(j, end=' ')
    print()
