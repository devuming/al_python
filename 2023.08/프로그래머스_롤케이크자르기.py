from collections import Counter


def solution(topping):
    answer = 0
    d_cnt = Counter(topping)
    s_top = set()

    for t in topping:
        d_cnt[t] -= 1
        s_top.add(t)
        if d_cnt[t] == 0:
            d_cnt.pop(t)
        if len(d_cnt) == len(s_top):
            answer += 1

    return answer


print(solution([1, 2, 1, 3, 1, 4, 1, 2]))  # 2
print(solution([1, 2, 3, 1, 4]))  # 0
