# 기하_백준_하키
# 하키 링크는 (X, Y)가 가장 왼쪽 아래 모서리인 W * H 크기의 직사각형과, 반지름이 H/2이면서 중심이 (X, Y+R), (X+W, Y+R)에 있는 두 개의 원
# 선수들의 위치가 주어질 때, 링크 안 또는 경계에 있는 선수가 총 몇 명인지 구하는 프로그램
import sys, math
w, h, x, y, p = map(int, sys.stdin.readline().rstrip().split())
count = 0
r = h // 2

for _ in range(p):
    a, b = map(int, sys.stdin.readline().rstrip().split())

    if x <= a <= x + w and y <= b <= y + h:
        count += 1
        continue
    
    dist1 = math.sqrt((a - x) ** 2 + (b - (y + r)) ** 2)
    dist2 = math.sqrt((a - (x + w)) ** 2 + (b - (y + r)) ** 2)
    if dist1 <= r or dist2 <= r:
        count += 1

print(count)