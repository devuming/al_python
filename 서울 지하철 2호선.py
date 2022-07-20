# 서울 지하철 2호선
# 첫째 줄에 역의 개수 N(3 ≤ N ≤ 3,000), 둘째 줄부터 N개의 줄에는 역과 역을 연결하는 구간의 정보 \
# 임의의 두 역 사이에 경로가 항상 존재하는 노선만 입력으로 주어진다.
# 출력 : 총 N개의 정수를 출력한다. 1번 역과 순환선 사이의 거리, 2번 역과 순환선 사이의 거리, ..., N번 역과 순환선 사이의 거리를 공백으로 구분해 출력
# 못풀음
from re import A


def find(parent, i):
    if i != parent[i]:
        parent[i] = find(parent, parent[i])   

    return parent[i]

def find_distance(parent, i):
    distance = 1
    if parent[i] == 0:
        return 0
    else:
        distance += find_distance(parent, parent[i])
        return distance

def union(parent, a, b):
    p_a = find(parent, a)
    p_b = find(parent, b)

    if p_a < p_b:
        print('a', a, cycle[a], parent)
        if cycle[a]:
            parent[b] = a
        else:
            parent[b] = p_a
    else:
        print('b', cycle[b], parent)
        if cycle[b]:
            parent[a] = b
        else:
            parent[a] = p_b

n = int(input())

edges = []
parent = [i for i in range(n + 1)]
cycle = [False] * (n + 1)

for i in range(1, n + 1):
    edges.append(list(map(int, input().split())))

edges.sort(key=lambda x : x[0])
print(edges)
for edge in edges:
    a, b  = edge
    print(a, b)
    parent_a = find(parent, a)
    parent_b = find(parent, b)

    if parent_a != parent_b:
        union(parent, a, b)
    else:   # 사이클 발생
        for i in range(1, n + 1):
            if parent[i] == parent_a:
                cycle[i] = True
        
print(parent)
print(cycle)

# # 수 세기

# for i in range(1, n + 1):
#     counts[i] = find_distance(parent, parent[i])

# for i in range(1, n+ 1):
#     print(counts[i], end=" ")
