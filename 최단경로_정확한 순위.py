# 정확한 순위_플로이드 사용
# 학생들의 성적을 비교한 결과가 주어질때,
# 성적 순위를 정확히 알 수 있는 학생의 수 출력
# 한 학생이 모든 학생으로 도달이 가능하다면, 성적 순위를 정확하게 알 수 있다. **

from collections import deque
INF = 999999

def solution(n, rank):  # 학생 수, 비교 결과
    d = [[INF] * (n+1) for _ in range(n + 1)]
    for i in range(1, n+1):
        d[i][i] = 0     # 본인 = 0

    for r in rank:      # 비교할 수 있는 학생인 경우, 1 (간선이 있다고 본다)
        d[r[0]][r[1]] = 1   # (a, b) - a < b 일 경우
    
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
                
    # 순위 예측 가능한 학생의 수
    answer = 0
    for i in range(1, n + 1):
        count = 0 
        for j in range(1, n + 1):
            if d[i][j] != INF or d[j][i] != INF:
                count += 1
        
        if count == n:      # 비교 가능한 학생수가 총 학생수와 같다면
            answer += 1     # 순위 예측 가능

    return answer 


print(solution(6, [[1, 5], [3, 4], [4, 2], [4, 6], [5, 2], [5, 4]]))   # [a, b] : a < b