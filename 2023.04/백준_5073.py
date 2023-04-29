while True:
    nums = list(map(int, input().split()))
    nums.sort()
    a, b, c = nums

    if (a, b, c) == (0, 0, 0):
        break
    if c >= a + b:
        print("Invalid")
    else:
        if a == b == c:
            print("Equilateral")
        elif a == b or b == c:
            print("Isosceles")
        else:
            print("Scalene")