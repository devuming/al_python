# 최대 연속 부분수열의 합
arr = list(map(int, input().split()))

def getMaxSubsequence(arr):
    result = 0      # 최대 연속 부분 수열 합
    temp = 0        # 현재 합
    for i in range(len(arr)):
        temp += arr[i]
        result = max(temp, result)

        if temp <  0:
            temp = 0
    return result

# 모든 원소가 음수인 경우 = 원소 중 가장 큰값이 최대 연속 부분 수열
def getMaxElement(arr):
    return max(arr)

# main
result = getMaxSubsequence(arr)

if result == 0:     # 모든 원소가 음수인 경우
    print(getMaxElement(arr))
else:
    print(result)