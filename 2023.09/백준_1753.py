import sys
import heapq
INF = 10e9
v, e = map(int, sys.stdin.readline().rstrip().split())
k = int(sys.stdin.readline().rstrip())

edges = [[] for _ in range(v + 1)]
visited = [False] * (v + 1)
dist = [INF] * (v + 1)
dist[k] = 0

for _ in range(e):
    a, b, w = map(int, sys.stdin.readline().rstrip().split())
    edges[a].append((b, w))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0
    visited[start] = True

    while q:
        d, now = heapq.heappop(q)

        if dist[now] < d:
            continue

        for j in edges[now]:
            cost = dist[now] + j[1]

            if cost < dist[j[0]]:
                dist[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))


dijkstra(k)
for i in range(1, v + 1):
    if dist[i] == INF:
        print('INF')
    else:
        print(dist[i])
