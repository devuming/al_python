# 2019 KAKAO BLIND RECRUITMENT > 실패율
# 풀이 1 > 테스트22 케이스에서 실패
# def solution(N, stages):
#     answer = []
#     fail = {}           # 스테이지의 클리어 못한 플레이어수  
#     total = {}           # 스테이지의 도달한 플레이어수  
#     fail_rate = []
    
#     for s in stages:
#         if s < N + 1 :     
#             fail[s] = fail.get(s, 0) + 1    # 멈춰 있는 플레이어 수            
#         elif s == N + 1 :   # N + 1까지 도달 : 마지막 스테이지까지 도달 -> 실패한 count 증가 X            
#             s = N           # 도달한 플레이어 수 N단계까지 증가하기 위해 s 값 조절
        
#         for i in range(1, s + 1):
#             total[i] = total.get(i, 0) + 1          # 도달한 플레이어 수 

    
#     for i in range(1, N + 1):
#         fail_rate.append([i, fail.get(i, 0) / total.get(i, 1)])     # [단계, 실패율]
        
#     fail_rate.sort(key = lambda x: x[1], reverse=True)        # 실패율 순으로 정렬
    
#     for i in fail_rate:
#         answer.append(i[0])

#     return answer

# 풀이2
def solution(N, stages):
    fail_rate = {}
    
    players = len(stages)
    for i in range(1, N + 1):
        if players > 0:
            fail = stages.count(i)              # 멈춰 있는 플레이어 수   
            fail_rate[i] = fail / players       # 실패율
            players -= fail                     # 다음단계 총 플레이어수 감소
        else :
            fail_rate[i] = 0                    # 도달한 플레이어 수 0 이면 실패율 0
        
    fail_rate = sorted(fail_rate, key=lambda x:fail_rate[x], reverse=True)        # 실패율 순으로 정렬

    return fail_rate

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))        # [3, 4, 2, 1, 5]
print(solution(4, [4,4,4,4,4]))                     # [4, 3, 2, 1]