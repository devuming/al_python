# def solution(n, lost, reserve):     # 전체 학생 수, 도난당한 학생들의 번호 배열, 여벌의 체육복을 가져온 학생들의 번호 배열 
#     answer = 0      # 체육 수업을 들을 수 있는 학생의 최댓값

#     answer = n - len(lost)      # 아무에게도 못 빌려줬을 경우 체육수업을 들을 수 있는 학생 수
#     count = [0] * (n + 1)        # 학생 별 가지고 있는 체육복 수 

#     for i in range(1, n + 1):
#         if i not in lost:  # 도난 당하지 않은 사람 체육복 갯수 + 1
#             count[i] += 1
#         if i in reserve:   # 여벌의 체육복 있는 사람 체육복 갯수 + 1
#             count[i] += 1

#     print(count)
#     for i in range(1, n + 1):
#         if count[i] < 2:
#             continue

#         pre_student = 0     # 앞번호 학생
#         next_student = 0    # 뒷번호 학생

#         if i == 0 :
#             pre_student = 0
#             next_student = i + 1
#         elif i == (n - 1):
#             pre_student = i - 1
#             next_student = 0
#         else :
#             pre_student = i - 1   # 여벌 체육복 있는 학생의 앞 번호
#             next_student = i + 1  # 여벌 체육복 있는 학생의 뒷번호
        
#         for j in lost:
#             if (pre_student == int(j) or next_student == int(j)) and count[int(j)] == 0:  # 앞, 뒤 학생 중 한명이고, 빌린 체육복이 없다면
#                 count[i] -= 1
#                 count[j] = 1
#                 answer = answer + 1
#                 break
#         print(count) 

#     return answer

# 다시 풀기 (2022.04.04)
def solution(n, lost, reserve):     # 전체 학생수, 도난된 학생/여벌있는 학생 리스트
    answer = 0      # 수업을 들을 수 있는 학생의 최댓값

    s_reserve = list(set(reserve) - set(lost))        # 빌려줄 수 있는 학생 
    s_lost = list(set(lost) - set(reserve))           # 체육복 없는 학생
    
    for stud in s_reserve:    # 여벌이 있는 학생 앞뒤 확인
        if stud - 1 in s_lost:        # 앞의 학생이 잃어버렸으면
            s_lost.remove(stud - 1)   # 빌려줌
        elif stud + 1 in s_lost:      # 뒤의 학생이 잃어버렸으면
            s_lost.remove(stud + 1)   # 빌려줌
    
    answer = n - len(s_lost)  # 전체 학생수 - 체육복 못 빌린 학생들 = 체육수업 들을 수 있는 학생수
        
    return answer


print(solution(5, [2,4], [1, 3, 5]))    # 5
print(solution(5, [2, 4], [3]))         # 4
print(solution(3, [3], [1]))            # 2
print(solution(2, [2, 3], [2]))         # 1