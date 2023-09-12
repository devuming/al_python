import heapq


def solution(operations):
    min_h = []
    for operation in operations:
        op, num = operation.split()
        # print(op, num, end=' : ')
        if op == 'I':
            heapq.heappush(min_h, int(num))
        else:
            if len(min_h) > 0:
                if int(num) == -1:
                    # 최솟값 삭제
                    heapq.heappop(min_h)
                else:
                    # 최댓값 삭제
                    min_h = heapq.nlargest(len(min_h), min_h)[1:]
                    heapq.heapify(min_h)
        # print(min_h)
    if len(min_h) == 0:
        return [0, 0]
    return [heapq.nlargest(1, min_h)[0], min_h[0]]


print(solution(["I 16", "I -5643", "D -1",
      "D 1", "D 1", "I 123", "D -1"]))  # [0,0]
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45",
      "I 97", "D 1", "D -1", "I 333"]))  # [333, -45]
print(solution(["I -77", "I 56", "I 653", "D 1", "I -642", "D -1", "I -45",
      "I -97", "D 1", "D -1", "I 333", "D -1"]))  # [333, -45]
