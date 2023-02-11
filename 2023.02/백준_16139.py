# 백준 16139 인간-컴퓨터 상호작용
# 특정 문자열 S, 특정 알파벳 alpha와 문자열의 구간 
# [l,r]이 주어지면 S$의 l번째 문자부터 r번째 문자 사이에 alpha가 몇 번 나타나는지 구하는 프로그램
import sys

s = sys.stdin.readline().rstrip()
count = [[0] * 26]
# count = {0 : [0] * 26}

q = int(sys.stdin.readline().rstrip())
for i, ch in enumerate(s):
    count.append(count[len(count) - 1][:])
    # count[i + 1] = count[len(count) - 1][:]
    count[i + 1][ord(ch) - 97] += 1

for _ in range(q):
    alpha, l, r = sys.stdin.readline().rstrip().split()
    answer = count[int(r) + 1][ord(alpha) - 97] - count[int(l)][ord(alpha) - 97]
    print(answer)