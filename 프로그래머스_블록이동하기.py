# 프로그래머스_블록이동하기
# bfs 이동을 해보자
from collections import deque

def solution(board):
    n = len(board)
                 
    board2 = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            board2[i + 1][j + 1] = board[i][j]

    queue = deque()
    start = {(1, 1), (1, 2)}
    queue.append((0, start))
    visited = [start]
    
    # BFS 탐색
    while queue:
        t, pos = queue.popleft()
                 
        if (n, n) in pos:
            return t
        
        # 상하좌우 이동
        for next_pos in get_next_pos(board2, pos):
            if next_pos not in visited:
                queue.append((t + 1, next_pos))
                visited.append(next_pos)
    
    return 0

def get_next_pos(board, pos):    
    next_p = []
    pos = list(pos)
    pos_x1, pos_y1, pos_x2, pos_y2 = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
      
    # 상하좌우 이동
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in dirs:
        nx1, ny1 = pos_x1 + dx, pos_y1 + dy
        nx2, ny2 = pos_x2 + dx, pos_y2 + dy
                 
        if (board[nx1][ny1], board[nx2][ny2]) == (0, 0):
            next_p.append({(nx1, ny1), (nx2, ny2)})
                 
    # 가로일때 회전
    if pos_x1 == pos_x2:
        for i in [-1, 1]:   # 위아래칸 확인
            if (board[pos_x1 + i][pos_y1], board[pos_x2 + i][pos_y2]) == (0, 0):
                next_p.append({(pos_x1, pos_y1), (pos_x1 + i, pos_y1)})
                next_p.append({(pos_x2, pos_y2), (pos_x2 + i, pos_y2)})    
                 
    # 세로일때 회전
    elif pos_y1 == pos_y2:
        for i in [-1, 1]:   # 좌우칸 확인
            if (board[pos_x1][pos_y1 + i], board[pos_x2][pos_y2 + i]) == (0, 0):
                next_p.append({(pos_x1, pos_y1), (pos_x1, pos_y1 + i)})
                next_p.append({(pos_x2, pos_y2), (pos_x2, pos_y2 + i)})
    
    return next_p

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))      # 7