def solution(n, lost, reserve):
    answer = 0
    
    s = set(reserve) & set(lost)    # 여벌있는 학생 중 도난당한 학생
    
    reserve = list(set(reserve) - s)    # 여벌있는 학생 중 도난당한 학생 제거
    lost = list(set(lost) - s)
    n = n - len(lost)                   # 전체 학생수에서 도난 당한 학생 수 제거
    
    
    # 해시로 가지고 있는 체육복 수 관리
    h_reserve = {}
    for r in reserve:
        h_reserve[r] = h_reserve.get(r, 0) + 1
        
    for l in lost:
        if h_reserve.get(l - 1, 0) > 0:        # 앞번호 학생
            h_reserve[l - 1] -= 1        
            n += 1                             # 수업 들을 수 있는 학생 수 증가
            
        elif h_reserve.get(l + 1, 0) > 0:      # 뒷번호 학생
            h_reserve[l + 1] -= 1         
            n += 1                             # 수업 들을 수 있는 학생 수 증가
        
    return n       # 체육 수업을 들을 수 있는 학생의 최댓값

print(solution(5, [2, 4], [1, 3, 5]))   # 5
print(solution(	5, [2, 4], [3]))        # 4