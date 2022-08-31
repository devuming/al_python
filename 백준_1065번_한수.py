# 백준_함수_1065번 한수 
# 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 
# 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 

def hansu(x):
    if x // 10 == 0:
        return True

    nums = list(map(int, str(x)))
    step = nums[1] - nums[0]

    for i in range(2, len(nums)):
        if step != nums[i]- nums[i-1]:
            return False

    return True

n = int(input())

count = 0
for i in range(1, n + 1):
    if hansu(i):
        count += 1

print(count)
