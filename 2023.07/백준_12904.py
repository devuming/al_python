s = list(input())
t = list(input())

while True:
    if len(s) == len(t):
        if s == t:
            print(1)
        else:
            print(0)
        break
    end = t.pop()

    if end == 'B':
        t = t[::-1]
