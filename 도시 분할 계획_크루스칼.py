# 도시 분할 계획
# 유지비를 최소화하고 마을안에서는 경로가 있는 두개의 마을로 분할
# 크루스칼 사용
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b :
        parent[b] = a
    else:
        parent[a] = b
        

# 집과 길 갯수
n, m = map(int, input().split())
edges = []
parent = [0] * (n + 1)

# parent 배열의 부모 노드 자기 자신으로 초기화
for i in range(1, n + 1):
    parent[i] = i

for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()        # 비용 순으로 간선 정렬
result_cost = 0     # 유지비 최소값
last = 0            # 비용이 가장 큰 최소신장트리의 마지막 간선

for edge in edges:
    cost, a, b = edge

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result_cost += cost
        last = cost

result_cost -= last     # 비용이 가장 큰 간선을 제거하여 마을을 2개로 분리
print(result_cost)