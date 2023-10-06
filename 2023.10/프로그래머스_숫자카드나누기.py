def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)


def isDivisible(gcd, arr):
    for num in arr:
        if num % gcd == 0:
            return True
    return False


def solution(arrayA, arrayB):
    answer = 0
    gcd_a = arrayA[0]
    gcd_b = arrayB[0]
    for i in range(1, len(arrayA)):
        gcd_a = gcd(gcd_a, arrayA[i])

    for i in range(1, len(arrayB)):
        gcd_b = gcd(gcd_b, arrayB[i])

    if not isDivisible(gcd_a, arrayB):
        if answer < gcd_a:
            answer = gcd_a
    if not isDivisible(gcd_b, arrayA):
        if answer < gcd_b:
            answer = gcd_b

    return answer


print(solution([10, 17], [5, 20]))  # 0
print(solution([10, 20], [5, 17]))  # 10
print(solution([14, 35, 119], [18, 30, 102]))  # 7
