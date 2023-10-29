import sys
n, k = map(int, sys.stdin.readline().rstrip().split())
loc = list(sys.stdin.readline().rstrip())
count = 0
for i, l in enumerate(loc):
    if l == 'P':
        for j in range(max(i - k, 0), min(i + k + 1, n)):
            if loc[j] == 'H':
                loc[j] = '-'
                count += 1
                break
print(count)
