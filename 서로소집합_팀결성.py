# 팀결성
# 0 : 팀합치기, 1 : 같은팀 여부 확인
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
    op, a, b = map(int, input().split())

    if op == 0 :    # 팀합치기
        union_parent(parent, a, b)
    elif op == 1:   # 같은 팀 여부 확인
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES')
        else:
            print('NO')