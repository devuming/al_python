n = int(input())
s = list(map(int, input().split()))
s.sort()
result = 10e9

for i in range(n):
    result = min(result, s[i] + s[(2*n) - i - 1])

print(result)
