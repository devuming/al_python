# 케빈베이컨 : 케빈 베이컨의 수가 가장 작은 사람을 출력   
# 플로이드 워셜 알고리즘 구하기
import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
graph = [[0] * n for _ in range(n)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a - 1][b - 1] = 1
    graph[b - 1][a - 1] = 1

for i in range(n):
    for j in range(n): 
        for k in range(n):
            if j == k:
                continue            

            if graph[j][i] and graph[i][k]: # j에서 i를 거쳐 k로 갈 수 있다면
                if graph[j][k] == 0:    # j - k 연결되지 않은 경우
                    graph[j][k] = graph[j][i] + graph[i][k]
                else:
                    graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])
result_idx = 0
min_count = 10e9
for i in range(n):
    count = 0
    for j in range(n):
        count += graph[i][j]   # i의 케빈 베이컨 수 구하기
    if min_count > count:
        min_count = count
        result_idx = i

print(result_idx + 1)