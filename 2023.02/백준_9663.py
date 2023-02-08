# 백준 9663 N-Queen
# N-Queen : N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제
# 퀸을 놓는 방법의 수를 구하는 프로그램
def promising(row):
    # 같은열과 대각선상에 있으면 안됨
    for i in range(row):
        if col[row] == col[i] or row - i == abs(col[row] - col[i]):
            return False
    return True
        

def nQueen(row):
    global count, col
    
    if row == n:
        count += 1
        return
    for x in range(n):
        col[row] = x

        if promising(row):
            nQueen(row + 1) # 다음행

n = int(input())
count = 0
col = [0] * (n)     # row 행에 놓이는 퀸의 열 위치
nQueen(0)
print(count)