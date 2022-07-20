# 위상정렬_커리큘럼_try2
# 선수강의가 있을 수 있는 N개의 강의에 대해, 수강하기까지 걸리는 최소시간을 각각 출력
from collections import deque
from copy import deepcopy

n = int(input())
indegree = [0] * (n + 1)        # 위상 정렬
graph = [[] for i in range(n + 1)]
time = [0] * (n + 1)
q = deque()

for i in range(1, n + 1):
    data = list(map(int, input().split()))
    time[i] = data[0]       # 수강시간
    for x in data[1 : -1]:
        indegree[i] += 1
        graph[x].append(i)

for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)

result = deepcopy(time)
while q:
    now = q.popleft()    

    for i in graph[now]:
        result[i] = max(result[i], result[now] + time[i])   # 이번 과목을 듣는 것과 안듣는 것의 최댓값
        indegree[i] -= 1        # 진입차수 감소

        if indegree[i] == 0:    # 새롭게 진입차수가 0이 된 과목 큐에 삽입
            q.append(i)

for i in range(1, n + 1):
    print(result[i])

    



        
