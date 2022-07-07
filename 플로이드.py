# 플로이드 : 모든 도시의 쌍 (A,B)에 대하여 A->B 최소비용
# 점화식 d[i][j] = min(d[i][j], d[i][k] + d[k][j])
INF = 999999

def floyd(n, edges):        # 도시의 수(노드), 버스의 수(간선), 버스의 정보(간선)
    path = [[INF] * n for _ in range(n)]

    for i in range(n):  # O(n)
        path[i][i] = 0  # 본인노드 비용 0

    # 간선정보로 거리 업데이트
    for e in edges:     # O(m)
        a = e[0] - 1
        b = e[1] - 1
        if path[a][b] > e[2]:     # 가장 짧은 비용만 저장
            path[a][b] = e[2]     # 비용
    for p in path:
        print(p)

    # 각 노드별 최소 거리 계산 : O(n^3)
    for k in range(n):      # 거쳐가는 노드
        for i in range(n):
            for j in range(n):
                path[i][j] = min(path[i][j], path[i][k] + path[k][j])

    return path

path = floyd(5, [[1, 2, 2], [1, 3, 3], [1, 4, 1], [1, 5, 10], [2, 4, 2], [3, 4, 1], [3, 5, 1], [4, 5, 3], [3, 5, 10], [3, 1, 8], [1, 4, 2], [5, 1, 7], [3, 4, 2], [5, 2, 4]])

for p in path:
    for cost in p:
        if cost == INF:
            print(0, end=' ')
        else:
            print(cost, end=' ')
    print()