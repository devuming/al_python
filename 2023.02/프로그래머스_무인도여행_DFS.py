import sys
sys.setrecursionlimit(10**5)        # Python의 최대 재귀 깊이(프로그래머스 : 100,000 -> 1,000,000)를 늘려 런타임 오류 해결됨

def dfs(maps, visited, x, y):
    if maps[x][y] == 'X' or visited[x][y]:
        return 0        
    
    visited[x][y] = True    # 방문처리    
    count = 0
    dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]   # 상하좌우
    for dx, dy in dirs:
        nx = x + dx
        ny = y + dy

        if nx >= 0 and nx < len(maps) and ny >= 0 and ny < len(maps[0]):
            count += dfs(maps, visited, nx, ny)    

    return int(maps[x][y]) + count
                     
def solution(maps):
    answer = []
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != 'X' and not visited[i][j]:
                result = dfs(maps, visited, i, j)
                answer.append(result)

    return sorted(answer)if len(answer) > 0 else [-1]

print(solution(["X591X","X1X5X","X231X", "1XXX1"])) # [1, 1, 27]
print(solution(["XXX","XXX","XXX"])) # [-1]