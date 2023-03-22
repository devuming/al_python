# 이중 우선순위 큐
# 우선 순위가 가장 높은 데이터 또는 낮은 데이터 중 하나를 삭제함
# 데이터 삭제 연산 > 우선 순위가 가장 높은 데이터 또는 가장 낮은 데이터 삭제
import heapq, sys
t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    min_q = []      # 최소힙
    max_q = []      # 최대힙
    visited = [False] * 1_000_001   # 동기화위한 배열 : True 면 큐에 유지
    k = int(sys.stdin.readline().rstrip())

    # 연산 입력
    for i in range(k): 
        op, num = sys.stdin.readline().rstrip().split()
        num = int(num)
        if op == 'I': # 삽입
            heapq.heappush(min_q, (num, i))
            heapq.heappush(max_q, (-num, i))
            visited[i] = True   # 힙에 유지
        elif max_q and op == 'D': # 삭제
            if num == 1:    # 최댓값 삭제
                while max_q and not visited[max_q[0][1]]:   # 삭제 됐는데 최대힙에 데이터 남아있으면
                    heapq.heappop(max_q)    # 삭제
                if max_q:
                    visited[max_q[0][1]] = False
                    heapq.heappop(max_q)
            elif num == -1: # 최소값 삭제
                while min_q and not visited[min_q[0][1]]:   # 방문처리 안됐으면
                    heapq.heappop(min_q)
                if min_q:
                    visited[min_q[0][1]] = False
                    heapq.heappop(min_q)
    # 삭제된 데이터 동기화 처리              
    while min_q and not visited[min_q[0][1]]:
        heapq.heappop(min_q)
    while max_q and not visited[max_q[0][1]]:
        heapq.heappop(max_q)
    # 최종적으로 최댓값과 최솟값을 출력
    if max_q:
        print((-1) * heapq.heappop(max_q)[0], end=" ")
        print(heapq.heappop(min_q)[0])
    else:
        print("EMPTY")