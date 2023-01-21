# 가장 큰수 - 못풀음
# def solution(numbers):  # numbers : 0또는 양의 정수가 담긴 배열
#     answer = ''         # 정수를 이어 붙여 만들 수 있는 가장 큰수

#     numbers = list(map(str, numbers))
#     numbers.sort(key=lambda x: x*3, reverse=True)      # 내림차순으로 정렬

#     # 첫번째 숫자가 가장 큰거 부터
#     print(numbers)
    
#     answer = ''.join(numbers)

#     return answer

# 다시 풀기 (2022.04.04)
def solution(numbers):
    answer = ''
    
    numbers = list(map(str, numbers))    
    numbers.sort(key=lambda x : (x * 4)[:4], reverse=True)  # 내림차순 정렬, 원소는 0이상 최대 1000이하 - 최대 네자리
    print(numbers)
    
    if numbers[0] == '0':
        answer = 0
    else :
        answer = ''.join(numbers)
    
    return answer       # 순서를 재배치해 만든 가장 큰수 

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
print(solution([0, 0, 100]))
print(solution([0, 0, 0]))
