from collections import deque


def solution(n, computers):
    answer = 0
    queue = deque([])
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            answer += 1
            queue.append(i)

            while queue:
                now = queue.pop()

                for j in range(n):
                    if now == j:
                        continue
                    if computers[now][j] == 1 and not visited[j]:
                        visited[j] = True
                        queue.append(j)

    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))  # 2
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))  # 1
