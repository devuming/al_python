# 팰린드롬 수
import sys
while True:
    num = sys.stdin.readline().rstrip()
    if num == '0':
        break

    if num == num[::-1]:
        print('yes')
    else:
        print('no')