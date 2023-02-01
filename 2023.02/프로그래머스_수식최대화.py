from itertools import permutations

def calc(n, op, exp):
    if n == 2:  # 가장 우선순위가 높은 연산자인 경우
        return str(eval(exp))        # 계산 결과 리턴
    # 각 연산자 기준으로 쪼개서 recursive 호출 -> return 값들 연산자로 합쳐 계산
    if op[n] == '+':
        return str(eval('+'.join([calc(n + 1, op, ex) for ex in exp.split('+')])))
    elif op[n] == '-':
        return str(eval('-'.join([calc(n + 1, op, ex) for ex in exp.split('-')])))
    else:
        return str(eval('*'.join([calc(n + 1, op, ex) for ex in exp.split('*')])))


def solution(expression):
    answer = 0
    op = list(permutations(['+', '-', '*'], 3)) # 우선순위 낮은 순
    
    for o in op:
        result = calc(0, o, expression)
        print(o, result)
        answer = max(answer, abs(int(result)))        # 결과값 중 큰 값(절대값)

    return answer
    
print(solution("100-200*300-500+20")) #	60420
print(solution("50*6-3*2")) #	300