# 백준 2738_행렬덧셈
# N*M 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램
import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(n):
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(m):
        matrix[i][j] += temp[j]

for i in range(n):
    print(' '.join([str(j) for j in matrix[i]]))