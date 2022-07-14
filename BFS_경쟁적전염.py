# 경쟁적 전염 : BFS
from collections import deque

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]     # 상하좌우 방향
matrix = []
position = []       # 바이러스 초기 위치 정보

# 시험관 크기 n, 바이러스 k가지
n, k = map(int, input().split())

# 시험관 정보(n * n)
for _ in range(n):
    matrix.append(list(map(int, input().split())))

s, virus_x, virus_y = map(int, input().split())

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] != 0:
            position.append((i, j, matrix[i][j], 0))      # (행, 열, 바이러스종류, 초)

# 바이러스 순서대로 정렬            
position.sort(key = lambda x:x[2])
queue = deque(position)

while queue:
    x, y, virus, sec = queue.popleft()

    if sec == s:    
        break

    for dir_x, dir_y in directions:
        nx = x + dir_x
        ny = y + dir_y

        if nx < 0 or ny < 0 or nx >= n or ny >= n:      # 이동 가능 범위 내인지 체크
            continue
        
        if matrix[nx][ny] == 0:                         # 다른 바이러스가 없는 경우에만
            matrix[nx][ny] = virus  # 증식
            queue.append((nx, ny, virus, sec + 1))      # 초 증가
    

print(matrix[virus_x - 1][virus_y - 1])     # s 초 뒤의 x, y 위치의 바이러스 종류


        