import sys
from collections import deque
while True:
    l, r, c = map(int, sys.stdin.readline().rstrip().split())
    if (l, r, c) == (0, 0, 0):
        break
    building = []
    for _ in range(l):
        floor = []
        for _ in range(r):
            floor.append(sys.stdin.readline().rstrip())
        building.append(floor)
        sys.stdin.readline().rstrip()
    dirs = [(0, 0, 1), (0, 0, -1), (0, -1, 0), (0, 1, 0),
            (1, 0, 0), (-1, 0, 0)]  # 동, 서, 남, 북, 상, 하
    queue = deque([])
    visited = [[[0] * c for _ in range(r)] for _ in range(l)]

    for i in range(l):
        for j in range(r):
            for k in range(c):
                if building[i][j][k] == 'S':
                    queue.append((i, j, k))
                    visited[i][j][k] = 0
                    break
            if queue:
                break
        if queue:
            break

    while queue:
        i, j, k = queue.popleft()
        if building[i][j][k] == 'E':
            break

        for df, dx, dy in dirs:
            nf = i + df
            nx = j + dx
            ny = k + dy
            if nf < 0 or nf >= l or nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue
            if building[i][j][k] == '#':
                continue
            if visited[nf][nx][ny] != 0:
                continue
            visited[nf][nx][ny] = visited[i][j][k] + 1
            queue.append((nf, nx, ny))

    if building[i][j][k] == 'E':
        print(f'Escaped in {visited[i][j][k]} minute(s).')
    else:
        print('Trapped!')
