# 완전탐색_카펫
import math
def solution(brown, yellow):
    answer = []
    
    # yellow의 약수
    for i in range(1, int(math.sqrt(yellow)) + 1):
        if yellow % i != 0:
            continue
        
        j = yellow // i
        a = i + 2
        b = j + 2
        if (a * b) - yellow == brown:
            return [b, a]
    
    return answer
print(solution(10, 2, [4, 3]))
print(solution(8, 1, [3, 3]))
print(solution(24, 24, [8, 6]))