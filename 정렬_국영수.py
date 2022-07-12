# 국영수
n = int(input())
score = []
for _ in range(n):
    score.append(tuple(input().split()))        # (이름, 국어점수, 영어점수, 수학점수)

score.sort(key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))  # 국어 내림차순-영어 오름차순-수학 내림차순-이름 오름차순

for s in score:
    print(s[0])     # 이름 출력