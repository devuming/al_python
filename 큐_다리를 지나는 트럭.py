# 다리를 지나는 트럭_스택/큐
# 모든 트럭이 다리를 건너려면 최소 몇초가 걸리는지
# 트럭은 1초에 1씩 전진
from collections import deque
def solution(bridge_length, weight, truck_weights):     # 다리 길이, 견딜수 있는 무게, 트럭의 무게
    wait_queue = deque(truck_weights)   
    bridge_queue = deque()   
    
    second = 1
    bridge_sum = wait_queue[0]
    bridge_queue.append([wait_queue.popleft(), 0])

    while bridge_queue:        
        second += 1
        for b in bridge_queue:
            b[1] += 1   # 트럭이 머무른 초 증가

        # 다리 다 건넜는지 확인
        if bridge_queue and bridge_queue[0][1] == bridge_length:
            bridge_sum -= bridge_queue[0][0]
            bridge_queue.popleft()

        if wait_queue:         # 건너야하는 트럭이 남은 경우       
            if len(bridge_queue) < bridge_length and bridge_sum + wait_queue[0] <= weight:
                bridge_sum += wait_queue[0]
                bridge_queue.append([wait_queue.popleft(), 0])

    return second

print(solution(2, 10, [7,4,5,6])) #	8
print(solution(100, 100, [10])) #	101
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10])) #	110