# 프로그래머스_혼자서하는 틱택토
def checkFinished(board, now):
    # 현재 위치 가로/세로 확인
    for i in range(3):
        i_cnt = 0       # 가로
        j_cnt = 0       # 세로
        for j in range(3):
            if board[i][j] == now:
                i_cnt += 1
            if board[j][i] == now:
                j_cnt += 1
        if i_cnt == 3:
            return True
        if j_cnt == 3:
            return True

    # 대각선 확인
    # 왼->오
    cnt = 0
    for i in range(3):
        if board[i][i] == now:
            cnt += 1
    if cnt == 3:
        return True
    # 오->왼 대각선
    cnt = 0
    for i in range(3):
        if board[i][2-i] == now:
            cnt += 1
    if cnt == 3:
        return True
    return False

def solution(board):
    o_count = 0
    x_count = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O':
                o_count += 1
            elif board[i][j] == 'X':
                x_count += 1

    if x_count - o_count > 0 or o_count - x_count > 1:
        return 0  
    if checkFinished(board, 'O'):
        if o_count == x_count:
            return 0  
    if checkFinished(board, 'X'):
        if o_count > x_count:
            return 0  

    return 1


# print(solution(["O.X", ".O.", "..X"]))   #	1
# print(solution(["OOO", "...", "XXX"]))   #	0
# print(solution(["...", ".X.", "..."]))   #	0
# print(solution(["...", "...", "..."]))   #	1
# print(solution(["XOO", ".X.", "..X"]))   #	0
print(solution(["XOO", ".XO", "..X"]))   #	1
print(solution(["XOX", "XOO", "X.O"]))   #	1
print(solution(["XO.", "XOO", "X.O"]))   #	0
print(solution(["XOX", "XO.", "X.O"]))   #	0
print(solution(["XO.", "XO.", "X.O"]))   #	1

# 9, 10, 37, 40, 44 실패
# 통과 -  if o_count < x_count 를 
# => if x_count - o_count > 0 or o_count - x_count > 1: 로 변경