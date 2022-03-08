# 서로소 집합 사용
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 정점, 간선 union 연산 횟수 입력
edges = []
result = 0
result_edges = []

v, e = map(int, input().split())

# 서로소 집합 부모노드 배열 초기화
parent = [0] * (v + 1)
for i in range(1, v + 1):
    parent[i] = i

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()        # 간선 : 오름차순 정렬

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b) : # 부모가 다르면 다른 서로소 집합에 속함
        union_parent(parent, a, b)
        result += cost
        result_edges.append((cost, a, b))

# 결과 출력
print('MST :')
for edge in result_edges:
    print(edge)
print('MST 비용 : ', result)
