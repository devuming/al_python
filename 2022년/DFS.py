# DFS (깊이 우선 탐색)
# 스택 사용
# 인접한 노드 중 가장 작은 노드 방문
def dfs(graph, v, visited):

    visited[v] = True
    print(v, end=' -> ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph = [[]
        , [2, 3, 8]
        , [1, 7]
        , [1, 4, 5]
        , [3, 5]
        , [3, 4]
        , [7]
        , [6, 8]
        , [1, 7]
]

visited = [False] * len(graph)

dfs(graph, 1, visited)