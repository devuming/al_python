# 백준 2477_참외밭
# 참외의 총개수 : 1m^2의 넓이에 자라는 참외 개수를 헤아린 다음, 참외밭의 넓이를 구하면 비례식을 이용
# 첫 번째 줄에 1m2의 넓이에 자라는 참외의 개수
# 임의의 한 꼭짓점에서 출발하여 반시계방향으로 둘레를 돌면서 지나는 변의 방향과 길이
k = int(input())
width, width_idx = 0, 0
height, height_idx = 0, 0
lines = []
for i in range(6):
    # 동 : 1, 서 : 2, 남 : 3, 북 : 4
    dir, size = map(int, input().split())
    lines.append((dir, size))
    if dir == 1 or dir == 2:
        if width < size:
            width = size
            width_idx = i
    else:
        if height < size:
            height = size
            height_idx = i

s_width = abs(lines[(width_idx - 1) % 6][1] - lines[(width_idx + 1) % 6][1])
s_height = abs(lines[(height_idx - 1) % 6][1] - lines[(height_idx + 1) % 6][1])

# 총 참외 : (전체 크기 - 작은 사각형) * 참외갯수
print((width * height - s_width * s_height) * k)