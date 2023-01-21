# 트리의 부모찾기

n = int(input())

edges = []
parent = [1 for _ in range(n + 1)]

for i in range(2, n + 1):
    edges.append(list(map(int, input().split())))

edges.sort(key = lambda x : x[0])

for edge in edges:
    a, b  = edge
    
    if parent[a] == 1:
        parent[b] = a
    elif parent[b] == 1:
        parent[a] = b    

print(parent)

