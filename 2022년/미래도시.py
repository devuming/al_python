INF = int(1e9)

# 회사의 갯수, 경로의 갯수 입력
n, m = list(map(int, input().split(' ')))

# 모든 경로를 무한대로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)] 

# 본인 -> 본인 회사 0으로 초기화
for a in range(n + 1):
    for b in range(n + 1):
        if a == b:
            graph[a][b] = 0
            
# 둘째 줄 ~ M + 1번째 줄 연결된 두 회사의 번호
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# x, k 회사 번호 입력
x, k = map(int, input().split(' '))

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[1][k] + graph[k][x]

# 도달할 수 없는 경우 -1
if distance >= INF :
    print(-1)
else:
    print(distance)
