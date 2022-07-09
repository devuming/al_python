# 모험가 길드 - 그리디

def solution(arr):
    answer = 0

    # 1. 정렬
    arr.sort()

    # 2. 작은 것부터 그룹 생성
    cnt =  0    # 현재 인원수
    for i in arr:
        cnt += 1
        if cnt >= i:
            answer += 1     # 그룹수 추가
            cnt = 0

    return answer

print(solution([2, 3, 1, 2, 2]))