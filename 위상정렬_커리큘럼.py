# 커리큘럽_위상정렬 이용
# 온라인 강의는 선수강의가 있을 수 있음
# 각 강의를 수강하기까지 걸리는 최소시간을 출력하는 프로그램
from collections import deque
import copy

# 듣고자 하는 강의의 수 입력
n = int(input())

graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)    # 진입 차수 관리
time = [0] * (n + 1)        # 각 강의 시간 관리

for i in range(1, n + 1):
    # 강의시간, 선수 과목 번호 입력
    data = list(map(int, input().split()))
    time[i] = data[0]   # 강의 시간

    for x in data[1:-1]:
        indegree[i] += 1    # 진입차수 증가(선수과목이 필요한 과목에 : i 과목의 선수과목 갯수)
        graph[x].append(i)  # 선수과목의 배열에 추가

def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    # 진입차수가 0인 노드 큐에 삽입
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
            
    while q:
        now = q.popleft() 

        for i in graph[now]:           
            result[i] = max(result[i], result[now] + time[i])     
            indegree[i] -= 1

            # 새롭게 진출차수가 0 이 되는 노드 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    for i in range(1, n + 1):
        print(i, '과목의 최소 수강시간 :', result[i])


topology_sort()