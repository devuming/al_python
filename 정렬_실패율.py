# 실패율
def solution(n, stages):        # 전체 스테이지 개수, 사용자가 멈춰있는 스테이지의 번호
    answer = []     # 실패율이 높은 스테이지 부터 내림차순으로 스테이지의 번호가 담긴 배열

    fail_rate = []
    players = len(stages)       # 전체 플레이어의 수 

    for i in range(1, n+1):     # 1번 스테이지 부터
        count = stages.count(i)                         # i번 스테이지에 멈춰있는 플레이어의 수
        
        if players == 0:
            fail = 0
        else:
            fail = count / players

        fail_rate.append((i, fail))
        players -= count
    
    # 내림차순 정렬
    fail_rate.sort(reverse=True, key=lambda x:x[1])        # 실패율 순으로 정렬

    for f in fail_rate:
        answer.append(f[0])     # 스테이지 번호만 담기

    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))        # [3, 4, 2, 1, 5]
print(solution(4, [4, 4, 4, 4, 4]))                 # [4, 1, 2, 3]