# def solution(id_list, report, k):       # 전체 유저, 신고(이용자id 신고한id), 정지기준
#     n = len(id_list)
#     mail = [0] * n
#     result = [[0] * n  for _ in range(n)]     # 신고 당한 횟수  
#     result_total = [0] * n 

#     for r in report:
#         a = id_list.index(r.split()[0]) # 이용자
#         b = id_list.index(r.split()[1]) # 신고자
        
#         result[b][a] += 1           # a > b 신고횟수 증가
        
#     for i in range(n):
#         for j in range(n):            
#             if result[i][j] > 0:
#                 result_total[i] += 1      # i의 신고 당한 횟수 증가

#     for i, r in enumerate(result_total):
#         if r >= k:
#             # 신고한 사람들에게 메일
#             for j, id in enumerate(result[i]):
#                 if id > 0:
#                     mail[j] += 1
        
#     return mail   # 각 유저가 받은 처리결과 메일 수

def solution(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}
    
    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))