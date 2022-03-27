# 큰수만들기
# 어떤 숫자에서 k 개의 수를 제거 했을 때 얻을 수 있는 가장 큰 숫자





def solution(number, k):        # 문자열형식의 숫자, 제거할 수의 갯수 k
    answer = ''                 # 만들 수 있는 가장 큰 숫자
    cnt = 0     # 제거 횟수
    iNumber = list(map(int,number))
    bNumber = [True] * len(iNumber)     # 동일한 크기의 배열 생성
     

    for i in range(0, len(iNumber) - 1):
        if iNumber[i] < iNumber[i+1]:   # 다음 자리 숫자보다 작으면 제거
            bNumber[i] = False
            cnt += 1

        if cnt == k:
            break
    
    for i in range(0, len(bNumber)):
        if bNumber[i]:
            answer += str(iNumber[i])

    return answer


print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))