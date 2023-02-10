# 백준 2566_최댓값
# 9×9 격자판에 쓰여진 81개의 자연수 또는 0이 주어질 때
# 이들 중 최댓값을 찾고 그 최댓값이 몇 행 몇 열에 위치한 수인지 구하는 프로그램
import sys
board = []

for _ in range(9):
    board.append(list(map(int, sys.stdin.readline().split())))

max_value = 0
x, y = 0, 0
for i in range(9):
    for j in range(9):
        if max_value < board[i][j]:
            max_value = board[i][j]
            x, y = i, j
print(max_value)
print(x + 1, y + 1)