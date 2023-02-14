# 단어 정렬
import sys
n = int(sys.stdin.readline().rstrip())
words = set()   # 중복제거
for _ in range(n):
    words.add(sys.stdin.readline().rstrip())

words = list(words)
words.sort(key=lambda x:(len(x), x))
for word in words:
    print(word)