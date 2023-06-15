# 비둘기의 집 원리 : n개의 방에 비둘기 n+1마리를 넣을 때, 어느 한방에는 반드시 2마리 이상이 있다.
# mbti 16개 중 3명 이상이 동일 -> 16 * (3 - 1) + 1 == 33
import sys
from itertools import combinations


def diff(a, b):
    cnt = 0
    for k in range(4):
        if a[k] != b[k]:
            cnt += 1

    return cnt


mbti = ['ISTJ', 'ISFJ', 'INFJ', 'INTJ', 'ISTP', 'ISFP', 'INFP', 'INTP',
        'ESTP', 'ESFP', 'ENFP', 'ENTP', 'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ']

d_mbti = {}
for i in range(16):
    m = mbti[i]
    if d_mbti.get(m) == None:
        d_mbti[m] = {}
    for j in range(16):
        d_mbti[m][mbti[j]] = diff(m, mbti[j])
# print(d_mbti)
t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    student = list(sys.stdin.readline().rstrip().split())
    if n >= 33:
        answer = 0
    else:
        student.sort()
        answer = 10e9

        c_stu = list(combinations(student, 3))

        for a, b, c in c_stu:
            dist = d_mbti[a][b] + d_mbti[b][c] + d_mbti[a][c]
            answer = min(dist, answer)

    print(answer)
