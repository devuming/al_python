import sys
n = int(sys.stdin.readline().rstrip())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(n):
    for j in range(n):
        for k in range(n):
            if graph[j][i] and graph[i][k]:
                graph[j][k] = 1

for i in range(n):
    for j in range(n):
        print(graph[i][j], end=' ')
    print()