# 그리디_조이스틱
# 조이스틱 조작 횟수 최솟값 구하기
def solution(name):
    answer = 0
    min_count = len(name) - 1
    
    while name[min_count] == 'A' and min_count > 0:
        min_count -= 1

    for i, char in enumerate(name):
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

        next_i = i + 1
        while next_i < len(name) and name[next_i] == 'A':
            next_i += 1
        
        min_count = min(min_count, i * 2 + len(name) - next_i)

    answer += min_count

    return answer

print(solution("JEROEN"))   # 56
print(solution("JAN"))      # 23
print(solution("AAA"))      # 0