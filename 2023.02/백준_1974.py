# 백준 1974 스택수열
# 스택에 push하는 순서는 반드시 오름차순
import sys

n = int(sys.stdin.readline().rstrip())
stk = []
answer = []
cur = 1
for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    while cur <= num:
        stk.append(cur)
        answer.append("+")
        cur += 1
    if stk[-1] == num:
        stk.pop()
        answer.append("-")
    else:
        answer = []
        break

if answer:
    print('\n'.join(answer))
else:
    print("NO")