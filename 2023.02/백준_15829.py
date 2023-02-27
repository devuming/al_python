# 백준 15829 해싱
def hashing(s_input):
    sum_value = 0
    for i, s in enumerate(s_input):
        sum_value += (ord(s) - 96) * (31 ** i)

    return sum_value % 1234567891

import sys
l = sys.stdin.readline().rstrip()
s_input = sys.stdin.readline().rstrip()   # 영문 소문자로만 이루어진 문자열
print(hashing(s_input))