import sys
n = int(sys.stdin.readline().rstrip())
grades = []
for _ in range(n):
    grades.append(int(sys.stdin.readline().rstrip()))

grades.sort()
result = 0
for i in range(1, n + 1):
    result += abs(i - grades[i - 1])
print(result)
