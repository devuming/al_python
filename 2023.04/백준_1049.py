import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
packs = []
pieces = []
for _ in range(m):
    pack, piece = map(int, sys.stdin.readline().rstrip().split())
    packs.append(pack)
    pieces.append(piece)

result1 = n * min(pieces)
result2 = 0
result2 += (n // 6) * min(packs)
n -= (n // 6) * 6

if n * min(pieces) > min(packs):
    result2 += min(packs)
else:
    result2 += n * min(pieces)

print(min(result1, result2))