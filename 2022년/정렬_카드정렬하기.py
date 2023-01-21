# 카드정렬하기
# A, B 카드 묶음을 하나로 만들기 위해 최소 몇번 비교가 필요한지
import heapq

n = int(input())
cards = []
for _ in range(n):
    heapq.heappush(cards, (int(input())))

result = 0
while len(cards) > 1:
    now = heapq.heappop(cards)
    now2 = heapq.heappop(cards)

    result +=  now + now2
    heapq.heappush(cards, now + now2)           # 연산 결과 추가

print(result)

