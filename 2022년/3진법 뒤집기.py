# 자연수 n이 매개변수로 주어집니다. n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.

def solution(n):
    answer = 0
    
    q = n // 3
    s = [(q, n % 3)]
    
    # 3진법 변환
    while q > 0:
        q = s[-1][0]        # 몫

        if q == 0: break

        s.append((q // 3, q % 3))       
    
    # 3진법 역수 10진법 표현
    for i, num in enumerate(s):
        power = len(s) - (i + 1)            # 자릿수
        answer += num[1] * (3 ** power)

    return answer

print(solution(45))
print(solution(125))