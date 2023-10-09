# dirs = {'d': (1, 0), 'l': (0, -1), 'r': (0, 1), 'u': (-1, 0)}
dirs = {'u': (-1, 0), 'r': (0, 1), 'l': (0, -1), 'd': (1, 0)}


def solution(n, m, x, y, r, c, k):
    stk = [(0, x - 1, y - 1, '')]

    while stk:
        cnt, nowx, nowy, route = stk.pop()

        for key, value in dirs.items():
            nx = nowx + value[0]
            ny = nowy + value[1]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            dist = abs(nx - (r - 1)) + abs(ny - (c - 1))
            if k - (cnt + 1) < dist:
                continue

            if (nx, ny) == (r - 1, c - 1):
                if (k - (cnt + 1)) % 2 == 1:
                    return "impossible"
                elif cnt + 1 == k:
                    return route + key

            stk.append((cnt + 1, nx, ny, route + key))
    return "impossible"


print(solution(3, 4, 2, 3, 3, 1, 5))  # "dllrl"
print(solution(2, 2, 1, 1, 2, 2, 2))  # "dr"
print(solution(3, 3, 1, 2, 3, 3, 4))  # "impossible"
