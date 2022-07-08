 # 행렬 테두리 변환
 # 시계 방향 이동
 # 회전되는 테두리의 최소값 구하기
def solution(rows, columns, queries):
    answer = []
    matrix = []
    # 1 ~ r * c 행렬 만들기
    for row in range(rows + 1):
        m = []
        for col in range(columns + 1): 
            if row != 0 and col != 0:
                m.append((row - 1) * columns  + col)
            else:
                m.append(0)
        matrix.append(m)

    for q in queries:
        x1, y1, x2, y2 = map(int, q)
        start = matrix[x1][y1]          # 시작 지점 값 변경에 따른 값 백업
        minvalue = matrix[x1][y1]       # 최소값 

        # 시계 반대 방향으로 값 가져오기
        # 1. 위로 이동 (아래의 값 위로 가져오기)
        for nx in range(x1, x2):
            matrix[nx][y1] = matrix[nx+1][y1]
            
            if matrix[nx][y1] < minvalue:
                minvalue = matrix[nx][y1]
            
        # 2. 우 -> 좌 이동 (오른쪽 값 왼쪽으로 가져오기)
        for ny in range(y1, y2):
            matrix[x2][ny] = matrix[x2][ny + 1]

            if matrix[x2][ny] < minvalue:
                minvalue = matrix[x2][ny]
        
        # 3. 아래로 이동 (위 값 아래로 가져오기)
        for nx in range(x2, x1, -1):
            matrix[nx][y2] = matrix[nx - 1][y2]
            
            if matrix[nx][y2] < minvalue:
                minvalue = matrix[nx][y2]
        
        # 4. 좌 -> 우 이동 (왼쪽값 오른쪽으로 가져오기)
        for ny in range(y2, y1, -1):
            matrix[x1][ny] = matrix[x1][ny - 1]

            if matrix[x1][ny] < minvalue:
                minvalue = matrix[x1][ny]

        # 마지막 값
        matrix[x1][y1+1] = start
        
        # 이동 완료 후 최소값 append
        answer.append(minvalue)

    
    return answer
    
print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))    #	[8, 10, 25]
print(solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))   #	[1, 1, 5, 3]
print(solution(100, 97, [[1,1,100,97]]))   #	[1]