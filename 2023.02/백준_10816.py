# 숫자 카드 2
import sys 
from collections import Counter
n = int(sys.stdin.readline().rstrip())
cards = list(map(int, sys.stdin.readline().rstrip().split()))
cnt_card = Counter(cards)

m = int(sys.stdin.readline().rstrip())
q_cards = list(map(int, sys.stdin.readline().rstrip().split()))
for q in q_cards:
    print(cnt_card.get(q, 0), end=' ')