import sys
n = int(sys.stdin.readline().rstrip())
likes = []
for _ in range(n ** 2):
    likes.append(list(map(int, sys.stdin.readline().rstrip().split())))
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
boards = [[0] * n for _ in range(n)]
for i in range(n ** 2):
    students = likes[i]
    pos = []
    for x in range(n):
        for y in range(n):
            if boards[x][y] == 0:
                blank = 0
                like = 0
                for dx, dy in dirs:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < n and 0 <= ny < n:
                        if boards[nx][ny] == 0:
                            blank += 1
                        if boards[nx][ny] in students[1:]:
                            like += 1
                
                pos.append([x, y, like, blank])
    pos.sort(key=lambda x:(-x[2], -x[3], x[0], x[1]))
    boards[pos[0][0]][pos[0][1]] = likes[i][0]

likes.sort(key=lambda x:x[0])
score = 0
for x in range(n):
    for y in range(n):
        idx = boards[x][y] - 1
        cnt = 0
        # 인접한 좋아하는 친구 수 세기
        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if boards[nx][ny] in likes[idx][1:]:
                cnt += 1
        score += int(10 ** (cnt - 1))

print(score)