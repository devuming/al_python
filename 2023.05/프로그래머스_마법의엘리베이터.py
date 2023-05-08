from collections import deque
def solution(storey):
    queue = deque([(storey, 0)])
    answer = 10e9
    while queue:
        print(queue)
        num, cnt = queue.popleft()

        if num == 0:
            answer = min(answer,cnt)
        if num < 10:
            answer = min(answer,cnt + num, cnt + (10 - num) + 1)
            continue

        minus = num % 10
        if minus == 0:
            queue.append((num // 10, cnt))
        else:
            plus = 10 - minus
            print(minus,plus)
            queue.append((num // 10, cnt + minus))
            queue.append((num // 10 + 1, cnt + plus))
    
    return answer

# print(solution(16)) # 6
# print(solution(2554)) # 16
# print(solution(1)) # 1
# print(solution(100000000)) # 1
# print(solution(155)) # 11
# print(solution(154)) # 10
print(solution(95)) # 6