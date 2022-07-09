# DFS 구현(재귀함수)
def dfs(graph, node, visited):
    visited[node] = True    # 방문처리
    print(node, end=' ')

    for g in graph[node]:
        if not visited[g]:  # 방문하지 않은 인접노드 방문
            dfs(graph, g, visited)

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

n = 8   # 노드 갯수
visited = [False] * (n + 1)
print(dfs(graph, 1, visited)) # 1번 노드부터 탐색