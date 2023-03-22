# 팩토리얼 결과 값의 뒤에서부터 0의 갯수를 구하는 프로그램
# (2 * 5) 의 갯수를 구하면 됨?
import sys
n = int(sys.stdin.readline().rstrip())
cnt = 0
while n >= 5:
    cnt += n // 5
    n //= 5
print(cnt)