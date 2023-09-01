import sys
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline().rstrip())
result = 0
graph = [[] * (n + 1) for _ in range(n+1)]

for _ in range(n-1):
    a, b, w = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append([b, w])


def dfs(node, weight):
    left, right = 0, 0

    for i, w in graph[node]:
        r = dfs(i, w)
        if left <= right:
            left = max(left, r)
        else:
            right = max(right, r)

    global result
    result = max(result, left + right)

    return max(left + weight, right + weight)


# 트리의 지름 = 왼쪽 최장 경로 + 오른쪽 최장경로
dfs(1, 0)
print(result)
