# 화성탐사 (2022.08.03 try1)
# N * N 공간에서 [0][0]-> [N-1][N-1] 로 이동하는 최소 비용 출력
# 다익스트라 방식
import heapq

INF = 9999999
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
t = int(input())

for _ in range(t):
    n = int(input())
    graph = []
    distance = [[INF] * n for _ in range(n)]    # [0][0]에서 각 칸으로 이동하기 위한 최소 비용
    q = []

    for _ in range(n):
        graph.append(list(map(int, input().split(' '))))
    
    x, y = 0, 0     # 출발 노드 
    heapq.heappush(q, (graph[x][y], x, y))        
    distance[x][y] = graph[x][y]

    while q:
        dist, x, y = heapq.heappop(q)
        
        if distance[x][y] < dist:
            continue
        for dx, dy in dir:
            nx = x + dx
            ny = y + dy

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            cost = distance[x][y] + graph[nx][ny]

            if cost < distance[nx][ny]:
                # 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드 선택
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))

    # [0][0]-> [N-1][N-1] 로 이동하는 최소 비용
    print(distance[n-1][n-1])
