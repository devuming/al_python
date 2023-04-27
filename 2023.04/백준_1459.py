# 걷기
import sys
x, y, w, s = map(int, sys.stdin.readline().rstrip().split())

# 가로 세로만 
a = x * w + y * w
# 대각선 + 평행
b = min(x, y) * s + abs(x - y) * w
# 대각선으로만
if (x + y) % 2 == 0:
    c = max(x, y) * s
else:
    c = (max(x, y) - 1) * s + w

time = min(a, b, c)
print(time)