# 신규아이디 추천
def solution(new_id):   # 입력된 아이디와 유사하면서 규칙에 맞는 아이디 추천해주는 프로그램    
    answer = []
    ## 조건 ##
    # 1. 길이는 3자이상 15자 이하
    # 2. 알파벳 소문자, 숫자, -, _, . 만 사용가능
    # 3. 단, .는 처음과 끝에 사용 불가, 연속으로도 사용 불가

    # 1. 대문자는 소문자로 치환
    for s in new_id.lower():        

        # 2. 알파벳 소문자, 숫자, -, _, . 가 아닌 문자 제거
        if not s.isalpha() and not s.isdigit() and s not in ['-', '_', '.']:
            continue
        
        # 3. . 가 2번이상 연속 > 하나로 치환 
        if s == '.' and (len(answer) > 0 and answer[-1] == '.'):
            continue

        answer.append(s)

    # 4. .가 처음과 끝에 위치하면 제거
    if len(answer) > 0 and answer[0] == '.':
            answer = answer[1:]
    if len(answer) > 0 and answer[-1] == '.' : 
            answer.pop()
        
    # 5. 빈 문자열이면 'a' 대입
    if len(answer) == 0:
        answer.append('a')

    # 6. 길이가 16자 이상이면 15자 이후 문자 제거, 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거
    answer = answer[:15] if len(answer) > 15 else answer
    if answer[-1] == '.': answer.pop()

    # 7. 2자 이하면 길이가 3이 될때까지 마지막 문자 반복
    while len(answer) < 3: answer.append(answer[-1])

    return ''.join(answer)   # 추천된 아이디

# print(solution("...!@BaT#*..y.abcdefghijklm"))      # "bat.y.abcdefghi"
# print(solution("z-+.^."))                           # "z--"
# print(solution(	"=.="))                             # "aaa"
# print(solution("123_.def"))                         # "123_.def"
print(solution(	"abcdefghijklmn.p"))                # "abcdefghijklmn"