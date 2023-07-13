def check(s):
    d_brac = {')': '(', '}': '{', ']': '['}

    stk = []
    for i in range(len(s)):
        if s[i] == ')' or s[i] == '}' or s[i] == ']':
            if stk and stk[-1] == d_brac[s[i]]:
                stk.pop()
            else:
                return False
        else:
            stk.append(s[i])

    if stk and len(stk) > 0:
        return False
    return True


def solution(s):
    answer = 0

    for i in range(len(s)):
        temp = s[i:] + s[:i]
        if check(temp):
            answer += 1
    return answer


print(solution("[](){}"))   # 3
print(solution("}]()[{"))   # 2
print(solution("[)(]"))     # 0
print(solution("}}}"))      # 0
