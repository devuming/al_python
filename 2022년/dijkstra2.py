# Dijkstra's Algorithm (Priority Queue)
# 가중치가 있는 방향성 그래프에서 한 특정 정점에서 다른 모든 정점으로 가는 최단 경로를 구하는 문제
# 시작점 : V1
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드의 갯수 간선의 갯수 입력
n, m = map(int, input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n + 1)]
# 방문한 적이 있는지 체크하는 목적의 리스트
visited = [False] * (n+1)
# 최단 거리 테이블 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보를 입력 받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a->b 비용 = c
    graph[a].append((b, c))

# 방문하지 않은 노드 중, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0   # 가장 최단 거리가 짧은 노드 인덱스

    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:  # distance의 값이 minvalue 보다 작고 방문하지 않은 경우
            min_value = distance[i]                     # distance의 값으로 최단 거리 갱신
            index = i                                   # 최단 거리 노드 인덱스 갱신

    return index

def dijkstra(start):
    # 시작 노드 초기화
    distance[start] = 0
    visited[start] = True      # 시작 노드 방문 처리
    for j in graph[start]:
        distance[j[0]] = j[1]   # start->j[0] 노드로 가는 거리로 distance 초기화
        
    # 시작 노드를 제외한 전체 n-1 개의 노드에 대해 반복
    for i in range(n - 1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node()
        visited[now] = True
        # 현재노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]

            if cost < distance[j[0]]:
                distance[j[0]] = cost

# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우, 무한출력
    if distance[i] == INF :
        print('무한')
    else:
        print(distance[i])
             
