import sys, heapq

heap = []   # 최대힙으로 사용할 리스트 생성
n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    x = int(sys.stdin.readline().rstrip())
    if x == 0:
        if heap:
            print(-heapq.heappop(heap)) # 배열에서 가장 큰 값 출력, 배열에서 제거
        else:
            print(0)
    else:
        heapq.heappush(heap, -x) # 추가 : 최대힙이므로 부호 반전해서 삽입