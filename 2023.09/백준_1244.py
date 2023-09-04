import sys
count = 20
n = int(sys.stdin.readline().rstrip())
switch = list(map(int, sys.stdin.readline().rstrip().split()))
s = int(sys.stdin.readline().rstrip())
for _ in range(s):
    g, num = map(int, sys.stdin.readline().rstrip().split())
    if g == 1:
        for i in range(num, n + 1, num):
            switch[i - 1] = 1 - switch[i - 1]
    else:
        switch[num - 1] = 1 - switch[num - 1]
        for i in range(1, n // 2 + 1):
            if (num - 1) - i < 0 or (num - 1) + i >= n:
                break
            if switch[(num - 1) - i] == switch[(num - 1) + i]:
                switch[(num - 1) - i] = 1 - switch[(num - 1) - i]
                switch[(num - 1) + i] = switch[(num - 1) - i]
            else:
                break

i = 0
while i <= n // count:
    if i == n // count and n % count == 0:
        break
    else:
        print(' '.join(map(str, switch[i * count:(i * count) + count])))
    i += 1
