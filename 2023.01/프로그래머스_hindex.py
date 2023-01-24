# 프로그래머스_H-Index
def solution(citations):
    right = max(citations)
    left = min(citations)
    
    while left <= right:
        h = (right + left) // 2   # h 최댓값
        count = 0
        for c in citations:
            if c >= h:
                count += 1
        print(right, left, h, count)
        if h < count:
            left = h + 1
        elif h > count:
            right = h - 1
        else:
            break
    # 이진 탐색
    return h

# print(solution([0, 10000]))     # 1
# print(solution([0, 1, 1, 1, 3, 4]))     # 2
print(solution([0, 0, 1, 1, 2]))     # 1
