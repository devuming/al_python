def bitcount_1(n, k):
    if n == 1:
        return k if k <= 2 else k - 1

    div = 5 ** (n - 1)
    loc = k // div
    cnt_1 = 4 ** (n - 1)  # 1의 갯수 : 4개씩 증가

    if k % div == 0:
        loc -= 1

    if loc < 2:
        return cnt_1 * loc + bitcount_1(n - 1, k - loc * div)
    elif loc == 2:
        return cnt_1 * loc
    else:
        return cnt_1 * (loc - 1) + bitcount_1(n - 1, k - loc * div)


def solution(n, l, r):
    return bitcount_1(n, r) - bitcount_1(n, l - 1)


print(solution(1, 2, 3))    # 1
print(solution(1, 2, 4))    # 2
print(solution(2, 4, 17))   # 8
