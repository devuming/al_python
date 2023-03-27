# 단지번호 붙이기
import sys
def dfs(x, y, num):
    global n
    if x < 0 or x >= n or y < 0 or y >= n:
        return
    if maps[x][y] != '1':
        return 
    
    maps[x][y] = num
    cnt[num - 1] += 1  # 단지 갯수 증가

    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in dirs:
        nx = x + dx
        ny = y + dy
        # 연결된 집 방문
        dfs(nx, ny, num)

n = int(sys.stdin.readline().rstrip())
maps = []
cnt = []        # 단지별 집의 수
for _ in range(n):
    maps.append(list(sys.stdin.readline().rstrip()))

num = 0
for i in range(n):
    for j in range(n):
        if maps[i][j] == '1':
            cnt.append(0)
            dfs(i, j, num)
            
# 총 단지 수
print(len(cnt))
# 집의 수 출력
cnt.sort()
for c in cnt:
    print(c)