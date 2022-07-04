import heapq
def solution(food_times, k):
    if sum(food_times) < k:
        return -1
    
    # 시간이 적은 음식부터
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))       # (먹는 시간, 음식번호)
    
    sum_value = 0   # 먹기 위해 사용한 시간
    pre_value = 0   # 직전에 다 먹은 음식 시간
    
    length = len(food_times)    # 음식 개수

    # sum_value + (현재 음식시간 - 이전음식시간) * 현재 음식 개수 와 k 비교
    while sum_value + ((q[0][0] - pre_value) * length) < k:
        now = heapq.heappop(q)[0]                   # 음식시간 작은것 부터 꺼내기
        sum_value += (now - pre_value) * length     # (현재 음식시간 - 이전음식시간) * 현재 음식 개수
        length -= 1                                 # 다먹은 음식 제외
        pre_value = now                             # 이전 음식 시간 재 설정
    
    result = sorted(q, key = lambda x:x[1])     # 음식 번호 기준으로 정렬
    return result[(k - sum_value) % length][1]  # 음식 번호 리턴

print(solution([3, 1, 2], 5))