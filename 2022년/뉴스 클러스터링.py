import math

def solution(str1, str2):
    answer = 0

    str1 = str1.upper()
    str2 = str2.upper()
    
    print(str1, str2)
    s1 = []
    s2 = []
    
    for i, s in enumerate(str1):
        if not s.isalpha():
            continue
        
        if i < len(str1) - 1 and str1[i+1].isalpha(): 
            s1.append(s + (str1[i+1]))

    for i, s in enumerate(str2):
        if not s.isalpha():
            continue

        if i < len(str2) - 1 and str2[i+1].isalpha(): 
            s2.append(s + (str2[i+1]))

    print(s1, s2)

    union = []
    inter = []

    for s in s1:
        union.append(s)

        if s in s2 : 
            inter.append(s)
            s2.remove(s)        # 첫번째 s 삭제
    
    for s in s2:
        union.append(s)

    print(inter)
    print(union)

    inter_cnt = 0 if len(inter) == 0 else len(inter)     # 겹치는 원소
    union_cnt =  1 if len(union) == 0 else len(union)        # 모든 원소 중 겹치는건 한번만 
    
    if str1 == str2:
        answer = 1
    else:
        answer = inter_cnt / union_cnt       # 자카드 유사도 = 교집합 / 합집합
    
    return math.trunc(answer * 65536)

print(solution('FRANCE',  'french'))	    # 16384
print(solution('handshake',	'shake hands'))	# 65536
print(solution('aa1+aa2',	'AAAA12'))	    # 43690
print(solution('E=M*C^2',	'e=m*c^2'))	    # 65536
print(solution('EM',	'C'))	            # 0