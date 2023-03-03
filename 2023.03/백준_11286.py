import sys, heapq

heap = []   
n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    x = int(sys.stdin.readline().rstrip())
    if x == 0:
        if heap:
            print(heapq.heappop(heap)[1]) 
        else:
            print(0)
    else:
        heapq.heappush(heap, (abs(x), x))   # 첫번째 원소 기준으로 최소힙 구성