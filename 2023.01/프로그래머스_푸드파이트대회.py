# 프로그래머스_푸드파이트대회

def solution(food):
    answer = '0'
    for i in range(len(food)-1, 0, -1):
        answer = str(i) * (food[i] // 2) + answer + str(i) * (food[i] // 2)
        
    return answer

print(solution([1, 3, 4, 6]))  # "1223330333221"
print(solution([1, 7, 1, 2]))	# "111303111"