# 2021 카카오 채용연계형 인턴십 > 숫자 문자열과 영단어
def solution(s):
    if s.isdigit():
        return int(s)
    answer = s
    alpha = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    for a in alpha:
        answer = answer.replace(a, str(alpha.index(a)))
    
    return int(answer)

print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))