# 금광
# n * m 크기의 금광
# 금광은 1 * 1 크기로, 특정 크기의 큼이 들어있음
# 첫번째 열의 어느 행에서든 출발 가능 
# m 번에 걸쳐 오른쪽 위, 오른쪽, 오른쪽 아래 3가지중 하나의 위치로 이동
# 얻을 수 있는 금의 최대의 크기를 출력
# 입력 : 테스트 케이스 T
#        매 테스트 케이스의 첫재줄에 n m 입력,
#        n * m의 위치에 매장된 금의 개수가 공백으로 구분되어 입력
# 출력 : 채굴자가 얻을 수 있는 금의 최대 크기 출력

for t in range(int(input())):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    d = []
    index = 0
    for i in range(n):
        d.append(array[index:index + m])
        index += m

    for j in range(1, m):
        for i in range(n):

            if i == 0 :
                left_top = 0
            else:
                left_top = d[i - 1][j - 1]
            if i == n - 1:
                left_down = 0
            else:
                left_down = d[i + 1][j - 1]

            left = d[i][j - 1]
            

            d[i][j] = d[i][j] + max(left, left_top, left_down)

    result = 0

    for i in range(n):
        result = max(result, d[i][m - 1])
    
    print(result)