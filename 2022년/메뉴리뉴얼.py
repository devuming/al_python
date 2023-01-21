# 메뉴 리뉴얼
# 단품 메뉴를 2개 이상의 단품요리를 갖는 코스요리로 구성
# 최소 2명이상의 손님으로부터 주문된 조합에 대해서만 메뉴 후보
from itertools import combinations
def solution(orders, course):       # 주문된 메뉴들, 구성하려는 단품메뉴의 갯수
    answer = []
    dict_combi = {}

    for order in orders:
        sorted(list(order))
        for c in course:
            combis = list(combinations(order, c))

            for i in range(len(combis)):
                combi = ''.join(sorted(list(combis[i])))
                dict_combi[combi] = dict_combi.get(combi, 0) + 1
    print(dict_combi)

    for key, value in dict_combi.items():
        if value >= 2:
            answer.append(key)
    
    return sorted(answer)       # 새로 추가하게 될 코스 요리의 메뉴 구성

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))   #	["AC", "ACDE", "BCFG", "CDE"]
# print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5])) #	["ACD", "AD", "ADE", "CD", "XYZ"]
# print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))                             #	["WX", "XY"]