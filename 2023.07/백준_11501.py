import sys
t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())

    stock = list(map(int, sys.stdin.readline().rstrip().split()))
    answer = 0

    i = n - 1
    j = i - 1

    while i > 0 and j >= 0:
        j = i - 1

        while j >= 0:
            if stock[i] <= stock[j]:
                i = j
                break

            answer += stock[i] - stock[j]
            j -= 1

    print(answer)
