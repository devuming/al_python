# 왕실의 나이트
# 8 * 8 좌표 평면에서 나이트가 이동할 수 있는 경우의 수 출력 
# 말을 타고 있기 때문에 L 자 형태로만 이동 가능
# 1. 수평으로 2칸 이동 수직 1칸 이동
# 2. 수직으로 2칸 이동 수평 1칸 이동
# 행 위치는 1~8로 표현, 열 위치는 a~h로 표현

x, y = 1, 1     # 초기 좌표
n = 8           # 좌표평면 8 * 8
steps = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]    # 나이트 이동가능 형태 정의

# 나이트 현재 위치 입력
location = input()
location_x = int(location[1])
location_y = int(ord(location[0])) - int(ord('a')) + 1   # 아스키코드로 입력 알파벳 a~h를 1~8로 변환

count = 0       # 이동 가능한 경우의 수

for step in steps:
    # x, y 좌표 이동
    x = location_x + step[0]
    y = location_y + step[1]

    # 유효한 위치면 경우의 수 증가
    if (x >= 1 and x <= n) and (y >= 1 and y <= n):
        count += 1

print(count)



