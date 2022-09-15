# 백준_1193_분수 찾기
# 이와 같이 나열된 분수들을 1/1 → 1/2 → 2/1 → 3/1 → 2/2 → … 과 같은 지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.
# X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.
x = int(input())

cnt = 0
line = 0
while cnt < x:
    line += 1
    cnt += line

m = cnt - x # 라인에서 몇번째
if line % 2 == 0:
    i = line - m
    j = m + 1
else:
    i = m + 1
    j = line - m

print(f'{i}/{j}')