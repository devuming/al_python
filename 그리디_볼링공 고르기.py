# 그리디_볼링공 고르기
# N개의 공의 무게가 주어질 때 두 사람이 볼링공을 고르는 경우의 수를 구하는 프로그램
# 각 볼링공은 최대 M까지의 무게를 가짐
n, m = map(int, input().split(' '))
ball = list(map(int, input().split(' ')))
ball.sort()

combi = []
for i in range(0, len(ball)):
    for j in range(i, len(ball)):
        if ball[i] != ball[j]:      # 서로 무게가 다른 공을 고름
            combi.append((ball[i], ball[j]))

print(len(combi))