# 서로소 집합을 활용한 사이클 판별 소스코드
def find_parent(parent, x):
    if parent[x] != x:
        find_parent(parent, parent[x])
    
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 정점, 간선 union 연산 횟수 입력
v, e = map(int, input().split())
parent = [0] * (v + 1)

for i in range(1, v + 1):
    parent[i] = i

cycle = False   # 사이클 발생 여부

# 간선 입력 받기
for i in range(e):
    a, b = map(int, input().split())

    # 사이클 발생시 union 안함
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True            # 둘이 부모가 같으면 cycle
        break
    # 사이클이 발생하지 않으면 union
    else:
        union_parent(parent, a, b)

if cycle:
    print('사이클 발생')
else:
    print('사이클 안발생')