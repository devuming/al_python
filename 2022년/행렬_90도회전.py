# 행렬 90도 회전 (오른쪽 방향)
def rotate_90_right(matrix):
    n = len(matrix)
    m = len(matrix[0])
    rotate =[[0] * n for _ in range(m)]

    # 회전
    for i in range(n):
        for j in range(m):
            rotate[j][n - i - 1] = matrix[i][j]

    return rotate

# 행렬 90도 회전 (왼쪽 방향)
def rotate_90_left(matrix):
    n = len(matrix)
    m = len(matrix[0])
    rotate =[[0] * n for _ in range(m)]

    # 회전
    for i in range(n):
        for j in range(m):
            rotate[j][i] = matrix[i][j]

    return rotate


matrix = [[0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1], 
        [2, 2, 2, 2, 2],
        [3, 3, 3, 3, 3],
        [4, 4, 4, 4, 4]]

for m in matrix:
    print(m)

print('----------')
rotate = rotate_90_right(matrix)

for r in rotate:
    print(r)

print('----------')
rotate = rotate_90_left(matrix)

for r in rotate:
    print(r)