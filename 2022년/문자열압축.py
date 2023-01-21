from collections import deque
# 문자열압축
def solution(s):
    answer = 1001       # s의 길이 최댓값 + 1로 초기화
    arr = list(map(str, s))    
        
    for step in range(1, len(s) + 1):
        stk = deque()

        for i in range(0, len(s), step):
            now = ''.join(arr[i:i+step])    # step 개 단위의 문자열
            cnt = 1                         # 중복 갯수

            if stk and stk[-1][0] == now:   # 이전문자열이 같으면
                last = stk.pop()    # pop 후 갯수 증가 
                cnt += last[1]      
                
            stk.append((now, cnt))          # (단위별문자열, 갯수) stack에 쌓기

        result = ''
        # 압축된 문자열
        while stk:
            now = stk.popleft()
            if now[1] > 1:
                result += str(now[1]) + now[0]   # 갯수 + 문자열
            else:
                result += now[0]            # 문자열만 add
        if answer > len(result):
            answer = len(result)

        print(step, result)

    return answer

print(solution("aa"))     # 2a, aa : 2
print(solution("aaa"))    # 3a : 2
print(solution("aa"))     # 2a, aa : 2

print(solution("aabbaccc"))     # 7
print(solution("ababcdcdababcdcd"))     #9
print(solution("abcabcdede"))     #	8
print(solution("abcabcabcabcdededededede"))     #	14
print(solution("xababcdcdababcdcd"))     #	17