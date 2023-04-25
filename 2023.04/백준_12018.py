import sys, heapq
n, m = map(int, sys.stdin.readline().rstrip().split())
heap = []
count = 0
for _ in range(n):
    p, l = map(int, sys.stdin.readline().rstrip().split())
    people = list(map(int, sys.stdin.readline().rstrip().split()))
    
    if p < l:
        heapq.heappush(heap, 1)
    else:
        people.sort(reverse=True)
        point = people[l - 1]
        if point == 36:
            heapq.heappush(heap, 36)
        else:
            heapq.heappush(heap, point)
while heap and heap[0] <= m:
    now = heapq.heappop(heap)
    m -= now
    count += 1
print(count)