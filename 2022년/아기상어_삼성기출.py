# 아기 상어 뚜루뚜뚜루
# N * N 공간에 물고기 M마리와 아기 상어 1마리가 있을 때, 
# 아기 상어는 상하좌우로 1칸씩 이동가능
# 자기 보다 큰 물고기가 있는 칸은 지나갈 수 없고, 작은 물고기만 먹을 수 있음
# 더이상 먹을 물고기가 없다면, 엄마 상어 도움 요청
# 먹을 수 있는 물고기가 1마리 보다 많으면 가장 가까운 물고기를 먹으러 간다
# 거리 - 지나가야하는 칸의 갯수의 최소값
# 초기 상어의 크기 = 2, 물고기 먹을 때마다 1씩 증가
# 9 = 아기상어의 위치, 칸 이동할 때마다 1초씩 증가
from collections import deque

def solution(n, space):     # 공간의 크기, 상태
    answer = 0              # 도움을 요청하지 않고 물고기를 잡아먹을 수 있는 시간
    visited = [[False] * (n + 1) for _ in range(n+1)]
    size = 2            # 초기 사이즈 = 2
    second = 0          # 머무른 시간
    queue = deque()

    for i in range(n):
        for j in range(n):
            if space[i][j] == 9:
                queue.append((i, j))
                break

    dx = [-1, 1, 0, 0]      # 상하좌우 x좌표
    dy = [0, 0, -1, 1]      # 상하좌우 y좌표
    while queue:
        now = queue.popleft()
        for i in range(4):
            nx = now[0] + dx[i]
            ny = now[0] + dy[i]
            
            if space[nx][ny] <= size and (nx > 0 and nx < n + 1 and ny > 0 and ny < n + 1) :    # 이동가능한 범위일 경우
                second += 0     # 이동
                
                if space[nx][ny] <=  size:
                    visited[nx][ny] = True    # 방문처리
                    if space[nx][ny] <  size:
                        # 먹기
                        space[nx][ny] = 0

    return answer

print(solution(3, [[0, 0, 0], [0, 0, 0], [0, 9, 0]]))       # 0
print(solution(3, [[0, 0, 1], [0, 0, 0], [0, 9, 0]]))       # 3
print(solution(4, [[4, 3, 2, 1], [0, 0, 0, 0], [0, 0, 9, 0], [1, 2, 3, 4]]))       # 14