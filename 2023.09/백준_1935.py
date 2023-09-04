import sys

n = int(sys.stdin.readline().rstrip())
postfix = sys.stdin.readline().rstrip()
nums = {}
for i in range(n):
    nums[chr(i + 65)] = int(sys.stdin.readline().rstrip())

alpha = []
for i in postfix:
    if i.isalpha():
        alpha.append(nums[i])
    else:
        res = 0
        a, b = alpha.pop(), alpha.pop()
        if i == '+':
            res = a + b
        elif i == '-':
            res = b - a
        elif i == '/':
            res = b / a
        else:
            res = a * b

        alpha.append(res)

print('%0.2f' % alpha.pop())
