import sys
from itertools import combinations
n = int(sys.stdin.readline().rstrip())
board = []
for _ in range(n):
    board.append(sys.stdin.readline().rstrip().split(' '))

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def checkStudent(x, y, o_block):
    for dx, dy in dirs:
        nx = x + dx
        ny = y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        # 바로 옆이 학생인 경우
        if board[nx][ny] == 'S':
            return False
        if (nx, ny) in o_block:
            continue
        # 장애물 전에 학생있는지 체크
        for i in range(2, n):
            nx = x + (dx * i)
            ny = y + (dy * i)
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if (nx, ny) in o_block:
                break
            if board[nx][ny] == 'S':
                return False
    return True


teachers = []
xys = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 'T':
            teachers.append((i, j))
        elif board[i][j] == 'X':
            xys.append((i, j))

comb = list(combinations(xys, 3))

for c in comb:
    flag = True
    for i, j in teachers:
        flag = checkStudent(i, j, c)

        if not flag:
            break
    if flag:
        print(c)
        break

if flag:
    print("YES")
else:
    print("NO")
