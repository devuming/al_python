def solution(n):
    answer = ''
    
    s = []
    q = n // 3
    r = n % 3

    if r == 0:
        s.append((q - 1, 4))
    else:
        s.append((q, r))

    while q > 0:
        q = s[-1][0]

        if q <= 0: break

        if q % 3 == 0:      # 나머지가 0이면
            s.append(((q // 3) - 1, 4))
        else:            
            s.append((q // 3, q % 3))
       

    for i in range(len(s) - 1, -1, -1):
        answer += str(s[i][1])      # 나머지 역순 출력
    return answer

print(solution(8))      # 22
print(solution(11))     # 42
print(solution(12))     # 44
print(solution(13))     # 111
print(solution(14))     # 112
print(solution(15))     # 114
print(solution(16))     # 121
print(solution(17))     # 122
print(solution(18))     # 124
print(solution(19))     # 141
print(solution(20))     # 142
print(solution(21))     # 144
print(solution(22))     # 211
print(solution(23))     # 212
print(solution(24))     # 214
print(solution(25))     # 221
print(solution(26))     # 222
print(solution(27))     # 224
print(solution(28))     # 241
print(solution(29))     # 242
print(solution(30))     # 244
print(solution(31))     # 411
