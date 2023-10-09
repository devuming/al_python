import sys
t = int(sys.stdin.readline().rstrip())
INF = int(10e9)
for _ in range(t):
    w = sys.stdin.readline().rstrip()
    k = int(sys.stdin.readline().rstrip())
    count = {}    # idx_list, cnt
    min_len = INF
    max_len = -1

    for i, a in enumerate(w):
        idx_list, cnt = count.get(a, ([], 0))
        idx_list.append(i)
        count[a] = (idx_list, cnt + 1)
        if len(idx_list) >= k:
            size = i - idx_list[-k] + 1
            min_len = min(min_len, size)
            max_len = max(max_len, size)

    if min_len == INF:
        print(-1)
    else:
        print(min_len, max_len)
