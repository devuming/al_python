# 백준 9663 N-Queen
# N-Queen : N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제
# 퀸을 놓는 방법의 수를 구하는 프로그램
n = int(input())
count = 0

def promising(row):
    for i in range(row):
        if col[row] == col[i] or row - i == abs(col[row] - col[i]):
            return False
    return True

def nQueen(row):
    global count

    if row == n:
        count += 1
        return
    for i in range(n):
        col[row] = i        # row행 i열  
        if promising(row):
            nQueen(row + 1)


col = [0] * n # i번째 행에 놓이는 컬럼 위치
nQueen(0)
print(count)