# 괄호변환
# 균형잡힌 괄호 문자열 = '('의 갯수와 ')'의 갯수가 같은 경우
# 올바른 괄호 문자열 = '('와 ')'의 짝이 맞는 경우

def balance_index_min(w):
    count = 0
    for i in range(len(w)):
        if w[i]== '(':
            count += 1
        else:
            count -= 1
        
        if count == 0:
            return i

def check_correct_str(w):
    stk = []
    for i in range(len(w)):
        if w[i] == '(':
            stk.append(w[i])
            continue
        if len(stk) == 0 or stk.pop() == ')':
            return False
        
    return len(stk) == 0

def solution(w):
    if w == '':
        return ''

    answer = ''
    # 1. 균형잡힌 문자열로 분리할 기준 index 구하기
    index = balance_index_min(w)

    # 2. u, v 로 분리 : u는 더이상 분리 불가능
    u = w[:index + 1]       # 0 ~ index
    v = w[index + 1:]       # index + 1 ~ 끝

    # u가 올바른 괄호 문자열인 경우
    if check_correct_str(u):
        answer = u + solution(v)
    # 올바른 괄호 문자열이 아닌 경우 
    else:
        answer += '('
        answer += solution(v)
        answer += ')'
        
        u_reverse = list(u[1:len(u) - 1]) # u의 앞뒤 문자 제거

        # 괄호방향을 뒤집음
        for i in range(len(u_reverse)):
            if u_reverse[i] == '(':
                u_reverse[i] = ')'
            else:
                u_reverse[i] = '('

        answer += ''.join(u_reverse)
        
    return answer

print(solution('(()())()'))     # (()())()
print(solution(')('))           # ()
print(solution('()))((()'))     # ()(())()