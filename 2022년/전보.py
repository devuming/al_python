# N개의 도시, X->Y로 향하는 통로가 있어야만 전보를 보낼 수 있음
# 통로를 거쳐 메세지를 보낼 때는 일정 시간이 소요됨

# C라는 도시에서 최대한 많은 도시로 메세지를 보내야 한다.
# 각 도시의 번호와 통로가 설치되어있는 정보가 주어졌을 때,
# 도시 C에서 보낸 메세지를 받는 도시의 갯수 & 모두 메세지를 받는데까지 걸리는 시간# Dijkstra's Algorithm (Priority Queue)
# 가중치가 있는 방향성 그래프에서 한 특정 정점에서 다른 모든 정점으로 가는 최단 경로를 구하는 문제
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드의 갯수, 간선의 갯수, 메세지 보내는 도시 C 입력
n, m, c = map(int, input().split())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n + 1)]
# 최단 거리 테이블 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보를 입력 받기
for _ in range(m):
    x, y, z = map(int, input().split())
    # x->y 비용 = z
    graph[x].append((y, z))

def dijkstra(start):    # 우선순위 큐 사용 다익스트
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:    # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0])) # 가장 인접한 노드정보 우선 순위 큐에 push
        

# 다익스트라 알고리즘 수행
dijkstra(c)

cnt = 0     # 메세지 받을 수 있는 도시 수 (연결된 도시만 메세지 받을 수 있음)
time = 0    # 도달할 수 있는 노드 중에서 가장 먼 노드까지 걸리는 시잔
for i in range(0, len(distance)):
    if distance[i] != INF and i != c:
        cnt += 1    # 메세지 받는 도시 갯수 증가
        time = max(time, distance[i])   # 메세지 받는데까지 걸리는 시간 

print('메세지를 받는 도시 수 : ' + str(cnt) + ' 걸리는 시간 : ' + str(time))
             
