# leetCode - 1944. Number of Visible People in a Queue
def solution(heights):
    answer = [0] * len(heights)
    stk = []
    
    for i in range(len(heights) - 1, -1, -1):
        count = 0
        while stk and heights[i] > stk[-1]:
            stk.pop()
            count += 1
        
        if stk :
            count += 1

        answer[i] = count
        stk.append(heights[i])

    return answer

print(solution([10,6,8,5,11,9]))    # [3, 1, 2, 1, 1, 0]
print(solution([5,1,2,3,10]))       # [4,1,1,1,0]