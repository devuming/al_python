def check(i, j, c, board):
    if i + 1 >= len(board) or j + 1 >= len(board[0]):
        return set()
    
    if c == board[i][j + 1] == board[i + 1][j] == board[i + 1][j + 1]:
        board[i][j + 1], board[i + 1][j], board[i + 1][j + 1] = '0', '0', '0'
        return set([(i, j + 1), (i + 1, j), (i + 1, j + 1)])
    else:
        return set()

def solution(m, n, board):
    count = 0
    board = list(map(list, board))
    pop = set()

    for i in range(m):
        for j in range(n):
            if i + 1 >= m or j + 1 >= n:
                continue
            if board[i][j] == '0':
                continue

            if board[i][j] == board[i][j + 1] == board[i + 1][j] == board[i + 1][j + 1]:
                pop.add((i, j))
                pop.add((i, j + 1))
                pop.add((i + 1, j))
                pop.add((i + 1, j + 1))
                pop |= check(i, j + 1, board[i][j], board)
                pop |= check(i + 1, j, board[i][j], board)                
                pop |= check(i + 1, j + 1, board[i][j], board)

                board[i][j], board[i][j + 1], board[i + 1][j], board[i + 1][j + 1] = '0', '0', '0', '0'
    
    # 위에서 내리기
    for i in range(m - 1, -1, -1):
        for j in range(n):
            x = i - 1
            while board[x][j] != '0':
                x -= 1

    for i in board:      
        print(i)
    print(len(pop))
    print(pop)   
         
    return count

print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"])) # 15
print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"])) # 14