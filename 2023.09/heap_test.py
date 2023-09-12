import heapq

# 1. 최소힙 생성
min_h = [-45, 33, 20, -90, 41]
heapq.heapify(min_h)

# 2. 최대값 삭제
min_h = heapq.nlargest(len(min_h), min_h)[1:]
heapq.heapify(min_h)
# print(min_h)


# 1. 힙의 아이템을 작은 순대로 3개 출력
heap = [-45, 33, 20, -90, 41]
heapq.heapify(heap)
print('작은 수 3개 : ', heapq.nsmallest(3, min_h))

# 2. 힙의 아이템을 큰 순대로 3개 출력
print('큰 수 3개 : ', heapq.nlargest(3, heap))
