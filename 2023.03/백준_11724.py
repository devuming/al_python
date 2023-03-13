# 연결요소의 개수
# 방향 없는 그래프가 주어졌을 때 연결 요소의 개수를 구하는 프로그램
import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
edges = []
parent = [i for i in range(0, n + 1)] # 정점의 부모

def find(v):
    if parent[v] != v:
        return find(parent[v])
    return v

def union(u, v):
    pu = find(u)
    pv = find(v)
    if pu < pv:
        parent[pv] = pu
    else:
        parent[pu] = pv
        
for _ in range(m):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    edges.append((u, v))

for edge in edges:
    u, v = edge
    if parent[u] != parent[v]:
        union(u, v)
        
# 최상위 부모 구하기        
answer = set()
for i in range(1, n + 1):
    answer.add(find(i))
    
print(len(answer))