# 카드
# 제일 위에 있는 카드를 버리고 제일 위 카드를 제일 밑으로 옮기는 것 반복
import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())

cards = deque([i for i in range(1, n + 1)])

while len(cards) > 1:
    cards.popleft()
    top = cards.popleft()
    cards.append(top)
print(cards.pop())
