# 백준 9012 괄호
import sys
t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    s_arr = list(sys.stdin.readline().rstrip())
    stk = []
    isVPS = True
    
    for i in range(len(s_arr)):
        if s_arr[i] == '(':
            stk.append(s_arr[i])
        else:
            if not stk or stk[-1] == ')':   # 괄호 짝이 안맞는 경우
                isVPS = False
                break
            else:
                stk.pop()

    if not stk and isVPS:    # 스택이 비어있는 경우 : VPS
        print("YES")
    else:
        print("NO")
