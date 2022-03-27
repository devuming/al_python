# 가장 큰수
def solution(numbers):  # numbers : 0또는 양의 정수가 담긴 배열
    answer = ''         # 정수를 이어 붙여 만들 수 있는 가장 큰수

    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)      # 내림차순으로 정렬

    # 첫번째 숫자가 가장 큰거 부터
    print(numbers)
    
    answer = ''.join(numbers)

    return answer


print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
