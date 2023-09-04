import sys
n, k = map(int, sys.stdin.readline().rstrip().split())
weights = list(map(int, sys.stdin.readline().rstrip().split()))


def dfs(total_w, date):
    global n, k
    if date == n:
        return 1

    count = 0
    total_w -= k
    if total_w < 500:
        return 0

    for i in range(n):
        if visited[i]:
            continue

        visited[i] = True
        count += dfs(total_w + weights[i], date + 1)
        visited[i] = False

    return count


count = 0
for i in range(n):
    visited = [False] * n
    visited[i] = True
    count += dfs(500 + weights[i], 1)

print(count)
