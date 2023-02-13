# 백준 2009_네번째 점
# 세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램
x_loc = {}
y_loc = {}
result = set()
for _ in range(3):
    x, y = map(int, input().split())
    x_loc[x] = x_loc.get(x, 0) + 1
    y_loc[y] = y_loc.get(y, 0) + 1

for k, v in x_loc.items():
    if v == 1:
        print(k, end=' ')
        break

for k, v in y_loc.items():
    if v == 1:
        print(k, end=' ')
        break