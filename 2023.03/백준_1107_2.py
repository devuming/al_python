# 채널 N으로 이동하기 위해 버튼을 최소 몇 번 눌러야 하는지를 출력
import sys
n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
nums = set(sys.stdin.readline().rstrip().split())

answer = abs(100 - n) # + 나 - 로 이동했을 경우 누르는 횟수

for i in range(1000001):
    channel = str(i)
    # if len(nums & set(channel)) > 0:
    if not nums.isdisjoint(set(channel)):   # 공통요소가 있는 경우
        # 고장난 번호와 교집합이 있는 경우 번호키로 이동하지 못하는 채널
        continue

    # 채널 i번으로 숫자키로 이동한 후 + 버튼을 누른 경우와 비교하여 최소 횟수 구하기
    answer = min(answer, len(channel) + abs(i - n)) 

print(answer)