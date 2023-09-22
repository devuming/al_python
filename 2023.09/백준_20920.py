import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
words = []
cnt = {}
for _ in range(n):
    word = sys.stdin.readline().rstrip()
    words.append(word)
    cnt[word] = cnt.get(word, 0) + 1

words.sort(key=lambda x: (-cnt[x], -len(x), x))
result = []
print('--------')
print(cnt)
print(words)
for word in words:
    if len(word) < m:
        continue
    if not result or result[-1] != word:
        result.append(word)
        print(word)
print(result)
