import sys
nums = sys.stdin.readline().rstrip()
result = []
for num in nums:
    result.append(int(num))

result.sort(reverse=True)
print(''.join(map(str, result)))