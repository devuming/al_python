# 프로그래머스_시소짝궁
# 2(m), 3(m), 4(m) 거리의 지점에 좌석이 하나씩
# 사람들의 몸무게 목록 weights이 주어질 때, 시소 짝꿍이 몇 쌍 존재하는지 구하여 return
from collections import Counter
def solution(weights):
    answer = 0
    weights.sort()
    d_weight = Counter(weights)
    pre_w = 0

    for w in weights:
        if pre_w == w:
            continue
        w_32 = w * (3/2) # 3(m)/2(m) : 1.5배
        w_43 = w * (4/3) # 4(m)/3(m)
        w_42 = w * 2 # 4(m)/2(m) : 2배

        # 2(m)/2(m)
        if d_weight.get(w, 0) >= 2:
            answer += 1
        # 2(m)/3(m)
        if d_weight.get(w_32, 0) > 0:
            answer += 1
        # 4(m)/3(m)
        if d_weight.get(w_43, 0) > 0:
            answer += 1
        # 4(m)/2(m)
        if d_weight.get(w_42, 0) > 0:
            answer += 1
        pre_w = w

    return answer

print(solution([100,180,360,100,270])) # 4
print(solution([100,200])) # 1
print(solution([200,200])) # 1
print(solution([100, 200, 300, 600])) # 3 (100-200, 200-300, 300-600)
print(solution([100, 200, 300, 400, 600])) # 3 (100-200, 200-300, 200-400, 300-600)
print(solution([150, 300, 225, 450, 600])) # 7 (150-300, 150-225, 225(3)-300(4), 225-450, 300(2)-450(3), 300-600, 450-600)