# 백준_10250_ACM 호텔
t = int(input())
for _ in range(t):
    answer = ''
    h, w, n = map(int, input().split())

    if n % h > 0:
        answer = str(n % h) + '{0:02d}'.format((n // h) + 1)
    else:
        answer = str(h) + '{0:02d}'.format(n // h)


    print(answer)