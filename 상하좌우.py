# 상하좌우.py
# 초기 좌표
x , y = 1 , 1

# 지도 크기 N 입력
n = int(input())

# 이동 계획서 입력
step = input().split()

# 방향별 x, y 이동 정의
way_en = ['L', 'R', 'U', 'D']
way_x = [0, 0, -1, 1]
way_y = [-1, 1, 0, 0]

for plan in step:                   # 계획
    for i in range(len(way_en)):    # 정의된 계획 문자 리스트 탐색
        if way_en[i] == plan : 
            x += way_x[i]           # x 좌표 이동
            y += way_y[i]           # y 좌표 이동

            if (x < 1 or x > n) or (y < 1 or y > n) : 
                x -= way_x[i]       # x 좌표 이동 취소
                y -= way_y[i]       # y 좌표 이동 취소
                continue

            break

# 결과 출력
print('(x , y) = (%d , %d)' % (x, y))