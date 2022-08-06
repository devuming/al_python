# 해시_위장
# 의상 종류 별로 하나씩만 입을 때, 만들 수 있는 조합의 수를 구해라
# 옷은 최소 한개 이상 입음
from itertools import combinations

def solution(clothes):
    answer = 0
    dict_cloth = {}
    
    for cloth in clothes:
        c_name = cloth[0]
        c_type = cloth[1]
        dict_cloth[c_type] = dict_cloth.get(c_type, [])
        dict_cloth[c_type].append(c_name)

    max_count = len(dict_cloth)
    i = 1
    while i <= max_count:       # i개의 종류의 옷을 입는 경우
        
        combis = list(combinations(dict_cloth, i))
        count = 0
        for combi in combis:
            count_i = 1
            for j in range(i):
                count_i *= len(dict_cloth[combi[j]])
            count += count_i
        answer += count

        i += 1   

    return answer

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))     # 3 + 2 =  5
print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"], ["blue jean", "바지"]]))     # 4 + (2 * 1) + (2 * 1) + (1 * 1) + (2 * 1 * 1)  =  4 + 2+ 2+ 1+ 2 = 11
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))     # 3
print(solution([["smoky_makeup", "face"]]))     # 1