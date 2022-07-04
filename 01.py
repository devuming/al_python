def solution(n, horizontal):
    answer = [[0] * n for _ in range(n)]       # 몇번째로 청소되었는지 표기
    n_sum = sum(range(1, n * n + 1)) # 총합

    step = 1
    r = 0
    c = 0
    answer[r][c] = step
    step += 1

    while r + 1 < n and c + 1 < n:        
        # 방향으로 한칸 이동
        if horizontal:
            c = c + 1
        else:
            r = r + 1
        
        answer[r][c] = step
        step += 1

        max_n = max(r, c)   # 행과 열의 max
        
        # 1
        for m in range(0, max_n):
            if horizontal :    # h == T : 오른쪽으로 이동
                r += 1
            
            if not horizontal: # h == F : 아래로 이동
                c += 1
             
            answer[r][c] = step
            step += 1

        # 2
        for m in range(max_n, 0, -1):
            if horizontal:      # h == T : 왼쪽으로 이동
                c -= 1
            
            if not horizontal:  # h == F : 위로 이동
                r -= 1
            
            answer[r][c] = step
            step += 1

        # 방향 변경
        horizontal = not horizontal

    return answer

print(solution(4, True))
print(solution(5, False))