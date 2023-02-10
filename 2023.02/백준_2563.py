# 백준 2563_색종ㅇ
# 가로 세로 크기가 100인 정사각형 도화지에 검은색 색종이(10*10) 붙일때 색종이의 영역을 구하는 프로그램
n = int(input())    # 색종이 수
location = []
point = set()
for _ in range(n):
    x, y = map(int, input().split())    # 왼쪽 하단 꼭지점 좌표
    location.append((x, y + 10))  # 왼쪽 상단 꼭지점 좌표 (정사각형 시작점)


for i, loc in enumerate(location):
    x = loc[0]
    y = loc[1]
    for x in range(loc[0], loc[0] + 10):
        for y in range(loc[1], loc[1] + 10):
            point.add((x, y))

print(len(point))