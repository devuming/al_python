# 문자열 재정렬
from unittest import result


def solution(text):
    eng = []
    value_sum = 0

    for s in list(text):
        if s.isalpha():
            eng.append(s)
        else:
            value_sum += int(s)
    eng.sort()
    
    return ''.join(eng) + str(value_sum)

print(solution('K1KA5CB7'))
print(solution('AJKDLSI412K4JSJ90'))