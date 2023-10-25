def turn(node, d):
    if node == 'L':
        return (d + 3) % 4
    elif node == 'R':
        return (d + 1) % 4
    return d


dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def solution(grid):
    answer = []
    n = len(grid)
    m = len(grid[0])
    visited = [[[False] * 4 for _ in range(m)]
               for _ in range(n)]

    for i in range(n):
        for j in range(m):
            for k in range(4):
                if visited[i][j][k]:
                    continue
                nx, ny, nd = i, j, k
                count = 0
                while not visited[nx][ny][nd]:
                    visited[nx][ny][nd] = True
                    count += 1
                    nd = turn(grid[nx][ny], nd)
                    nx = (nx + dir[nd][0]) % n
                    ny = (ny + dir[nd][1]) % m

                    if (nx, ny, nd) == (i, j, k) and count > 0:
                        answer.append(count)
                        break
    answer.sort()
    return answer


print(solution(["SL", "LR"]))  # [16]
print(solution(["S"]))  # [1,1,1,1]
print(solution(["R", "R"]))  # [4,4]
