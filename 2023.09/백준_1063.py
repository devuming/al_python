import sys
king, stone, n = sys.stdin.readline().rstrip().split()


def move(op, now_k):
    col, row = ord(now_k[0]), int(now_k[1])
    if op == 'R':  # 오른쪽 : 열 + 1
        if col < ord('H'):
            now_k[0] = chr(col + 1)
    elif op == 'L':  # 왼쪽 : 열 - 1
        if col > ord('A'):
            now_k[0] = chr(col - 1)
    elif op == 'B':  # 아래 : 행 - 1
        if row > 1:
            now_k[1] = str(row - 1)
    elif op == 'T':  # 위 : 행 + 1
        if row < 8:
            now_k[1] = str(row + 1)
    elif op == 'RT':  # 오른쪽 위 : 열 + 1, 행 + 1
        if col < ord('H') and row < 8:
            now_k[0] = chr(col + 1)
            now_k[1] = str(row + 1)
    elif op == 'LT':  # 왼쪽 위 : 열 - 1, 행 + 1
        if col > ord('A') and row < 8:
            now_k[0] = chr(col - 1)
            now_k[1] = str(row + 1)
    elif op == 'RB':  # 오른쪽 아래 : 열 + 1, 행 - 1
        if col < ord('H') and row > 1:
            now_k[0] = chr(col + 1)
            now_k[1] = str(row - 1)
    elif op == 'LB':  # 왼쪽 아래 : 열 - 1, 행 - 1
        if col > ord('A') and row > 1:
            now_k[0] = chr(col - 1)
            now_k[1] = str(row - 1)

    return ''.join(now_k)


for _ in range(int(n)):
    op = sys.stdin.readline().rstrip()
    n_king = move(op, list(king))

    if n_king == stone:  # 돌 위치 같은 경우 : 돌 위치 이동
        n_stone = move(op, list(stone))

        if n_stone != stone:
            king, stone = n_king, n_stone
    else:
        king = n_king
    # print(king, stone)

print(king)
print(stone)
