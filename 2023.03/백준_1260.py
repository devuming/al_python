# 그래프를 DFS 로 탐색한 결과와 BFS 로 탐색한 결과를 출력하는 프로그램
import sys
n, m, v = map(int, sys.stdin.readline().rstrip().split())
edges = []
for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    edges.append((a, b))
    edges.append((b, a))

edges.sort(key=lambda x:(x[0], x[1]))

def dfs(v):
    if visited_dfs[v]:
        return
    visited_dfs[v] = True
    dfs_v.append(str(v))   # 방문

    for e in edges:
        if e[0] == v:
            dfs(e[1])

from collections import deque
def bfs(v):
    queue = deque()
    queue.append(v)
    visited_bfs[v] = True

    while queue:
        now = queue.popleft()
        bfs_v.append(str(now))

        for e in edges:
            if e[0] == now and not visited_bfs[e[1]]:
                visited_bfs[e[1]] = True
                queue.append(e[1])

dfs_v = []
bfs_v = []
visited_dfs = [False] * (n + 1)
visited_bfs = [False] * (n + 1)
dfs(v)
bfs(v)

print(' '.join(dfs_v))
print(' '.join(bfs_v))