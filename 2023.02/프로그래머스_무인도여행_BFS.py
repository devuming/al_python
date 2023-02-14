from collections import deque

def bfs(maps, visited, x, y):  
    dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]   # 상하좌우  
    
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    count = 0

    while queue:
        now_x, now_y = queue.popleft()
        count += int(maps[now_x][now_y])        

        for dx, dy in dirs:
            nx = now_x + dx
            ny = now_y + dy

            if nx >= 0 and nx < len(maps) and ny >= 0 and ny < len(maps[0]):
                if maps[nx][ny] == 'X' or visited[nx][ny]:
                    continue
                queue.append((nx, ny))
                visited[nx][ny] = True

    return count
                     
def solution(maps):
    answer = []
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != 'X' and not visited[i][j]:
                answer.append(bfs(maps, visited, i, j))

    return sorted(answer)if len(answer) > 0 else [-1]

print(solution(["X591X","X1X5X","X231X", "1XXX1"])) # [1, 1, 27]
print(solution(["XXX","XXX","XXX"])) # [-1]