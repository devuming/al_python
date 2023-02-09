# 백준 14888_연산자 끼워넣기
# 수열과 연산자가 주어졌을때 만들수 있는 수식에서 결과가 최대인 것과 최소인 것을 구하는 프로그램
# 식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행
import sys
n = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
ops = list(map(int, sys.stdin.readline().rstrip().split()))  # 덧셈, 뺄셈, 곱셈, 나눗셈 갯수
max_val = -10e9
min_val = 10e9
dic_op = {0:'+', 1:'-', 2:'*', 3:'//'}

def solve(value, num):
    global max_val, min_val
    if num == n:
        max_val = max(max_val, value)
        min_val = min(min_val, value)
        return

    ori_value = value

    for i in range(4):
        if ops[i] > 0 :
            if value < 0 and i == 3:   # 음수를 양수로 나누는 경우
                value = eval(str(abs(value)) + dic_op[i] + str(nums[num]))
                value *= (-1)
            else:
                value = eval(str(value) + dic_op[i] + str(nums[num]))
            ops[i] -= 1
            solve(value, num + 1)
            value = ori_value
            ops[i] += 1

solve(nums[0], 1)
print(max_val)
print(min_val)