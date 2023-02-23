def dfs(land, score, x, y):
    global answer
    if x == len(land) - 1:
        answer = max(answer, score)
        return
    
    
    for j in range(len(land[x])):
        if j == y:
            continue
        score += land[x + 1][j]
        dfs(land, score, x + 1, j)
        score -= land[x + 1][j]

    return score
answer = 0

def solution(land):
    global answer

    for i in range(len(land[0])):
        dfs(land, land[0][i], 0, i)\

    return answer

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))    # 16
print(solution([[1,2,3,5],[5,7,9,8],[4,3,5,1]]))    # 5 + 9 + 4