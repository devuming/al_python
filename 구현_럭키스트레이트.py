# 럭키스트레이트
# 점수를 반으로 나누어 왼쪽 부분의 각 자릿수의 합과 오른쪽 부분의 각 자릿수의 합이 동일하면 럭키스트에리트
nums = list(input())

left = 0
right = 0

for i in range(len(nums)):
    if i < len(nums) // 2:
        left += int(nums[i])
    else:
        right += int(nums[i])

if left == right:
    print("LUCKY")
else:
    print("READY")