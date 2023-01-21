# 그리디_주유소
# 각 도시에 있는 주유소의 기름 가격과, 각 도시를 연결하는 도로의 길이를 입력으로 받아 제일 왼쪽 도시에서 제일 오른쪽 도시로 이동하는 최소의 비용을 계산하는 프로그램을 작성

# 현재 주유소랑 충전한 주유소 값 비교해서 싸면 현재 주유소의 기름으로 충전. 아니면 이전값
n = int(input())
dist = list(map(int, input().split()))
price = list(map(int, input().split()))

answer = 0
min_p = 10e9

for i in range(0, n - 1):
    if price[i] < min_p:
        min_p = price[i]
    answer += dist[i] * min_p

print(answer)