# N*M 크기의 직사각형
# 육지 : 0, 바다 : 1, 바다는 갈 수 없음 
# 0 : 북, 1 : 동, 2 : 남 , 3 : 서

# 1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향(반시계 방향으로 90도 회전한 방향) 부터 차례대로 갈 곳을 정한다
# 2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽방향으로 회전한다음 왼쪽으로 한칸 전진,
#   가보지 않은 칸이 없다면 왼쪽으로 회전
# 3. 모두 이미 가본 칸이거나 바다로 되어있는 칸인 경우 바라보는 방향을 유지한 태로 한칸 뒤로 가고 1단계로 돌아감
# 단, 뒤쪽 방향이 바다인 칸이면 움직임을 멈춤


# 방향 좌표 정의
way_x = [-1, 0, 1, 0]                           # 북동남서 x 이동 좌표
way_y = [0, 1, 0, -1]                           # 북동남서 y 이동 좌표

# 지도 입력
n, m = map(int, input().split())

visited_map = [[0] * m for _ in range(n)]           # 방문여부 체크 지도 0으로 초기화

# 현재 캐릭터의 x, y, 방향 입력
x, y, direction = map(int, input().split())
visited_map[x][y] = 1                               # 현재 위치 방문 확인

# 지도 입력 
in_map = []
for i in range(n) : 
    in_map.append(list(map(int, input().split())))  # 지도 입력 받기

#===== 왼쪽으로 회전하는 함수 =========
def turn_left() :
    global direction

    if direction == 0 : 
        direction = 3
    else :
        direction -= 1

#====================================
count = 1                                       # 방문한 칸의 수 (현재 있는 칸 +1)
turn_count = 0                                  # 회전 횟수

while True:
        # 왼쪽으로 회전
        turn_left()         

        # 방향 이동 시 x, y 좌표 계산
        nx = x + way_x[direction]
        ny = y + way_y[direction]

        # 정면에 칸이 있는지 체크
        if visited_map[nx][ny] == 0 and in_map[nx][ny] == 0 : 
            # 방문여부 체크
            visited_map[nx][ny] = 1
            
            # x, y 좌표 이동
            x = nx
            y = ny

            # 방문 칸 횟수 증가, 회전 횟수 초기화
            count += 1
            turn_count = 0
            continue

        # 이미 갔거나, 바다인 경우
        else :
            # 회전 횟수 증가
            turn_count += 1    

        # 북동서남 다 확인 했을 경우
        if turn_count == 4 :
            # 뒤로 이동 시 좌표 계산
            nx = x -  way_x[direction]
            ny = y - way_y[direction]

            # 바다가 아닌 경우
            if in_map[nx][ny] == 0 :
                # x, y 좌표 이동
                x = nx
                y = ny

                # 회전 횟수 0으로 초기화
                turn_count = 0

            # 바다 = 이동 불가
            else:
                # 종료
                break

# 이동 횟수 출력
print(count)


