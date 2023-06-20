import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())
edges = [[] for i in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    edges[a].append(b)
    edges[b].append(a)

parent = [i for i in range(n + 1)]
queue = deque([1])

while queue:
    now = queue.popleft()

    for v in edges[now]:
        if parent[v] == v and v != 1:
            parent[v] = now
            queue.append(v)

for i in range(2, n + 1):
    print(parent[i])
