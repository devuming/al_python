import sys
n = int(sys.stdin.readline().rstrip())
words = set()

for _ in range(n):
    words.add(sys.stdin.readline().rstrip())
    
print('\n'.join(sorted(words, key=lambda x:(len(x), x))))
