import sys
n, game = sys.stdin.readline().rstrip().split()
names = set()
for _ in range(int(n)):
    names.add(sys.stdin.readline().rstrip())

if game == 'Y':
    print(len(names))
elif game  == 'F':
    print(len(names) // 2)
else:
    print(len(names) // 3)