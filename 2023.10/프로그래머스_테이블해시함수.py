def xor(a, b):
    return a ^ b


def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key=lambda x: (x[col - 1], -x[0]))
    for i in range(row_begin, row_end + 1):
        s = 0
        for j in range(len(data[i - 1])):
            s += data[i - 1][j] % i
        answer = xor(answer, s)

    return answer


print(solution([[2, 2, 6], [1, 5, 10], [4, 2, 9], [3, 8, 3]], 2, 2, 3))   # 4
