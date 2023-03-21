# 색종이 만들기
import sys
sys.setrecursionlimit(10**7)
blue_cnt, white_cnt = 0, 0

def divide_paper(start_x, end_x, start_y, end_y):
    # 체크
    global blue_cnt, white_cnt
    blue_flag, white_flag = False, False
    for i in range(start_x, end_x):
        for j in range(start_y, end_y):
            if paper[i][j] == 0:
                white_flag = True   # 흰색이 칠해진 경우
            else:
                blue_flag = True

    if not white_flag:  # 흰색없는 경우  
        blue_cnt += 1   # 파란색 종이 수 증가
        return
    if not blue_flag: # 파란색없는 경우 
        white_cnt += 1
        return
    if end_x - start_x <= 1:
        return
    # 4개로 쪼개기
    mid_x = (end_x - start_x) // 2
    mid_y = (end_y - start_y) // 2
    divide_paper(start_x, start_x + mid_x, start_y, start_y + mid_y)
    divide_paper(start_x, start_x + mid_x, start_y + mid_y, end_y)
    divide_paper(start_x + mid_x, end_x, start_y, start_y + mid_y)
    divide_paper(start_x + mid_x, end_x, start_y + mid_y, end_y)
    
    
n = int(sys.stdin.readline().rstrip())
paper = []
for _ in range(n):
    paper.append(list(map(int, sys.stdin.readline().rstrip().split())))
divide_paper(0, n, 0, n)
print(white_cnt)
print(blue_cnt)