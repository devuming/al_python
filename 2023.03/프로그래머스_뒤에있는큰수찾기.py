import heapq
def solution(numbers):
    answer = [-1] * len(numbers)
    h = []

    for i, num in enumerate(numbers):

        while h and h[0][0] < num:
            value, idx = heapq.heappop(h)
            answer[idx] = num

        heapq.heappush(h, (num, i))
        
    return answer
        

print(solution([2, 3, 3, 5])) # [3, 5, 5, -1]
print(solution([9, 1, 5, 3, 6, 2])) # [-1, 5, 6, 6, -1, -1])