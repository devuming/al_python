# 백준 2580_스도쿠
# 가로줄, 세로줄에는 1-9의 숫자가 한번식만
# 3 * 3 정사각형 안에도 숫자가 한번씩만
import sys
def promising(row, col, n):
    # 같은 행에 있는지
    for x in range(len(sudoku)):
        if sudoku[row][x] == n:
            return False
    # 같은 열에 있는지
    for y in range(len(sudoku[0])):
        if sudoku[y][col] == n:
            return False
    # 3 * 3에 있는지
    r_start = row // 3 * 3
    c_start = col // 3 * 3
    for x in range(r_start, r_start + 3):
        for y in range(c_start, c_start + 3):
            if sudoku[x][y] == n:
                return False
    return True


def solve(n):       
    if n == len(blank):     # 모든 빈칸 다 채웠으면
        # 출력
        for i in range(9):
            for j in range(9):
                print(sudoku[i][j], end=' ')
            print()
        exit()      # 프로그램 종료
    
    for i in range(1, 10):
        x = blank[n][0]  # 빈칸의 x 좌표
        y = blank[n][1]  # 빈칸의 y 좌표
        if promising(x, y, i):
            sudoku[x][y] = i
            solve(n + 1)
            sudoku[x][y] = 0
    
    


sudoku = []
blank = []  # 채워야하는 칸의 좌표 저장   
for _ in range(9):
    sudoku.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            blank.append((i, j))
        
solve(0)    # 0번째 빈칸부터 스도쿠 채우기
