n = int(input())

for i in range(n):
    print(' ' * (n - i - 1), end='')
    print('*' * (2 * i + 1))

for i in range(1, n):
    print(' ' * i, end='')
    print('*' * (2 * n - 1 - (2 * i)))