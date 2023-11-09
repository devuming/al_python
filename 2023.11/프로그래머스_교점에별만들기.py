def getPoint(a1, b1, c1, a2, b2, c2):
    if a1 * b2 - b1 * a2 == 0:      # 평행하는 경우
        return None
    px = (b1 * c2 - c1 * b2) / (a1 * b2 - b1 * a2)
    py = (c1 * a2 - a1 * c2) / (a1 * b2 - b1 * a2)

    return (px, py)


def solution(line):
    answer = []
    # 교점 구하기
    point = []  # [(행,열)]
    x_point = []
    y_point = []

    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            a1, b1, c1 = line[i]
            a2, b2, c2 = line[j]
            if not getPoint(a1, b1, c1, a2, b2, c2):
                continue
            px, py = getPoint(a1, b1, c1, a2, b2, c2)
            if px != int(px) or py != int(py):
                continue
            # print(f'({px}, {py})')
            x_point.append(int(px))
            y_point.append(int(py))
            point.append((int(px), int(py)))

    min_x, max_x = min(x_point), max(x_point)
    min_y, max_y = min(y_point), max(y_point)
    print(min_x, max_x)
    print(min_y, max_y)
    # 교점 정렬
    point = list(set(point))
    point.sort(key=lambda x: (x[1], -x[0]))
    for i in range(max_y, min_y - 1, -1):   # y
        a = ''
        for j in range(min_x, max_x + 1):   # x
            if point and point[-1] == (j, i):
                a += '*'
                point.pop()
            else:
                a += '.'
        answer.append(a)

    return answer


# ["....*....", ".........", ".........", "*.......*", ".........", ".........", ".........", ".........", "*.......*"]
print(solution([[2, -1, 4], [-2, -1, 4],
      [0, -1, 1], [5, -8, -12], [5, 8, 12]]))
print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]))    # ["*.*"]
print(solution([[1, -1, 0], [2, -1, 0]]))    # ["*"]
print(solution([[1, -1, 0], [2, -1, 0], [4, -1, 0]]))    # ["*"]
