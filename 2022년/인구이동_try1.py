# 인구이동 문제
# 국경선을 공유하는 두 나라라의 인구차이가 L 이상 R 이하면 국경을 열고 연합
# 연합 후 각 칸의 인구수 = (연합의 인구수) / 연합을 이루고 있는 칸의 개수
# 인구 이동이 몇번 발생하는지 출력
from collections import deque

a = []      # 인구수 배열
count = 0   # 인구이동 횟수2

# 입력
N, L, R = map(int, input().split())
for _ in range(N):
    a.append(list(map(int, input().split())))

def union(i, j, index):
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]        # 상하좌우 순서

    queue = deque()   
    queue.append((i, j)) 
    
    sum_pop = 0         # 연합된 인구수
    count = 1           # 연합된 국가 갯수
    country = []        # 연합된 국가 인덱스
    union_country[i][j] = index

    while queue:
        row, col = queue.popleft()       # 현재 칸의 인구수

        sum_pop += a[row][col]
        country.append((row, col))

        # 상하좌우 칸 살펴보기
        for i in range(len(dir)):
            nx = row + dir[i][0]    # x좌표 이동
            ny = col + dir[i][1]    # y좌표 이동
                        
            if nx >= N or ny >= N or nx < 0 or ny < 0 or union_country[nx][ny] != -1:  # 이동가능 범위 체크
                continue

            near = a[nx][ny]        # 인접 칸

            if L <= abs(a[row][col] - near) and abs(a[row][col] - near) <= R:
                # 국경 개방
                queue.append((nx, ny))         
                union_country[nx][ny] = index   # 연합된 국가 인덱스로 변경 
                count += 1

    if len(country) == 1: return

    # 연합 인구 수 변경
    for r, c in country:
        a[r][c] = sum_pop // len(country)    

total = 0                                       # 이동 횟수
# N * N 이상.... 
# 연합
while True:
    index = 0
    union_country = [[-1] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if union_country[i][j] == -1:
                union(i, j, index)
                index += 1

    if index ==  N * N : # 연합된 국가가 없음2
        break

    total += 1      # 이동횟수 증가

print(total) # 인구이동 횟수