#  def solution(participant, completion):      # 참여 선수들, 완주한 선수들
#     answer = ''     # 완주하지 못한 선수의 이름

#     participant.sort()
#     completion.sort()

#     p_count = [1] * len(participant)

#     for item in completion:
#         for i in range(len(participant)):
#             if item == participant[i] and p_count[i] == 1:
#                 p_count[i] = 0    
#                 break

#     print(p_count)

#     for i in range(len(participant)):
#         if p_count[i] != 0:
#             answer = participant[i]
#             break

#     return answer 

def solution(participant, completion):      # 참여 선수들, 완주한 선수들
    answer = ''     # 완주하지 못한 선수의 이름
    p = {}
    c = {}

    # 동명이인 체크를 위해 각 참가자 별 인원 체크 - 딕셔너리 사용
    for item in participant:
        if p.get(item) :
            p[item] += 1
        else:
            p[item] = 0

    # 동명이인 체크를 위해 각 참가자 별 인원 체크 - 딕셔너리 사용
    for item in completion:
        if c.get(item) :
            c[item] += 1
        else:
            c[item] = 0

    # 참가자 딕셔너리에 없거나, 각 딕셔너리의 Value 값이 다르면 완주 X
    for item in participant:
        if item in c.keys():
            answer = item
            break
        elif c[item] != p[item]:
            answer = item
            break

    return answer

a = ["mislav", "stanko", "mislav", "ana"]
b = ["stanko", "ana", "mislav"]

print(solution(a, b))