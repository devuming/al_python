def solution(n, lost, reserve):     # 전체 학생 수, 도난당한 학생들의 번호 배열, 여벌의 체육복을 가져온 학생들의 번호 배열 
    answer = 0      # 체육 수업을 들을 수 있는 학생의 최댓값

    answer = n - len(lost)      # 아무에게도 못 빌려줬을 경우 체육수업을 들을 수 있는 학생 수
    count = [0] * (n + 1)        # 학생 별 가지고 있는 체육복 수 

    for i in range(1, n + 1):
        if i not in lost:  # 도난 당하지 않은 사람 체육복 갯수 + 1
            count[i] += 1
        if i in reserve:   # 여벌의 체육복 있는 사람 체육복 갯수 + 1
            count[i] += 1

    print(count)
    for i in range(1, n + 1):
        if count[i] < 2:
            continue

        pre_student = 0     # 앞번호 학생
        next_student = 0    # 뒷번호 학생

        if i == 0 :
            pre_student = 0
            next_student = i + 1
        elif i == (n - 1):
            pre_student = i - 1
            next_student = 0
        else :
            pre_student = i - 1   # 여벌 체육복 있는 학생의 앞 번호
            next_student = i + 1  # 여벌 체육복 있는 학생의 뒷번호
        
        for j in lost:
            if (pre_student == int(j) or next_student == int(j)) and count[int(j)] == 0:  # 앞, 뒤 학생 중 한명이고, 빌린 체육복이 없다면
                count[i] -= 1
                count[j] = 1
                answer = answer + 1
                break
        print(count)

    return answer

print(solution(3, [3], [1]))