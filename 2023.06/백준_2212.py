import sys
n = int(sys.stdin.readline().rstrip())
k = int(sys.stdin.readline().rstrip())
loc = list(map(int, sys.stdin.readline().rstrip().split()))
loc.sort()
sub = [0] * (n - 1)
for i in range(len(sub)):
    sub[i] = loc[i+1] - loc[i]

sub.sort()

print(sum(sub[:n-k]))
