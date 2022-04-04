# 큰수만들기
# 어떤 숫자에서 k 개의 수를 제거 했을 때 얻을 수 있는 가장 큰 숫자





# def solution(number, k):        # 문자열형식의 숫자, 제거할 수의 갯수 k
#     answer = ''                 # 만들 수 있는 가장 큰 숫자
#     cnt = 0     # 제거 횟수
#     iNumber = list(map(int,number))
#     bNumber = [True] * len(iNumber)     # 동일한 크기의 배열 생성
     

#     for i in range(0, len(iNumber) - 1):
#         if iNumber[i] < iNumber[i+1]:   # 다음 자리 숫자보다 작으면 제거
#             bNumber[i] = False
#             cnt += 1

#         if cnt == k:
#             break
    
#     for i in range(0, len(bNumber)):
#         if bNumber[i]:
#             answer += str(iNumber[i])

#     return answer

# 다시 풀어보기 (2022.04.04)
def solution(number, k):
    answer = ''
    numbers = list(map(str, number))
    collected = []
    
    for i, num in enumerate(numbers):   
        # 현재 수보다 앞의 수가 더 작으면 삭제
        while len(collected) > 0 and int(num) > int(collected[-1]) and k > 0:
            collected.pop()
            k -= 1     

        collected.append(num)
        
        if k == 0 and i < len(numbers): # k개만큼 수 제거했으면 반복 종료 및 나머지 수 붙이기
            collected += [numbers[j] for j in range(i + 1, len(numbers))]
            break
    
    answer = ''.join(collected) if k == 0 else ''.join(collected[:-k])      # 제거해야하는 갯수가 남은 경우에는 뒤에서 k개 제거
    
    return answer


print(solution("1924", 2))      # 94
print(solution("1231234", 3))    # 3234
print(solution("4177252841", 4))    # 775841

print(solution("4177252841", 0))    # 4177252841
print(solution("4177252841", 1))    # 4177252841

print(solution("1230", 3))    # 3