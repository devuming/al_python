# 스택 이용
def solution(numbers):
    answer = [-1] * len(numbers)
    stk = []

    for i, num in enumerate(numbers):

        while stk and numbers[stk[-1]] < num:
            idx = stk.pop()
            answer[idx] = num

        stk.append(i)
        
    return answer
        

print(solution([2, 3, 3, 5])) # [3, 5, 5, -1]
print(solution([9, 1, 5, 3, 6, 2])) # [-1, 5, 6, 6, -1, -1])