# 그리디_먹방라이브_try2
# 다시 풀어보기
import heapq    # 최소 힙 사용
def solution(food_times, k):
    # 더 섭취할 음식이 없는 경우 -1
    if sum(food_times) <= k:
        return -1

    q = []
    n = len(food_times)

    # 각 음식 별로 먹는 데 걸리는 시간 힙에 삽입
    for i, food in enumerate(food_times):
        heapq.heappush(q, (food, i + 1))

    sum_value = 0       # 먹기 위해 사용한 시간
    previous = 0

    while sum_value + ((q[0][0] - previous) * n) <= k:
        now = heapq.heappop(q)
        sum_value += (now[0] - previous) * n
        previous = now[0]
        n -= 1          # 다먹은 음식 갯수 감소

    # 남은 음식 번호기준 정렬
    q.sort(key = lambda x:x[1])

    return q[(k - sum_value) % n][1] 

print(solution([3, 1, 2], 5))       # 1
