# leetCode 278.First Bad Version
# isBadVersion() API 함수가 주어짐 -> 오류가 있는 버전이면 True 반환
# 에러가 발생한 이후의 버전은 모두 에러 발생, 처음 에러가 발생한 버전을 찾아라
# 선형 탐색 - 시간초과 발생 O(n) 의 복잡도
# -> 이진 탐색하는 것이 탐색 시간을 줄일 수 있을 것
class Solution(object):
    def __init__(self,bad):
        self.bad = bad

    def isBadVersion(self, version):  # 임의로 내가 구현
        if version >= self.bad:
            return True
        else:
            return False

    def firstBadVersion(self, n):
        # 이진 탐색 수행
        left = 1
        right = n
        bad = -1
        while left <= right:
            mid = (left + right) // 2
            if self.isBadVersion(mid):
                    # 이전 버전 체크
                right = mid - 1
                bad = mid
            else:
                left = mid + 1
        return bad

# 인스턴스 생성 시, 인자값을 첫번째 bad version 으로 설정
test1 = Solution(4)
test2 = Solution(1)
test3 = Solution(3)

print(test1.firstBadVersion(5)) # 4
print(test2.firstBadVersion(1)) # 1
print(test3.firstBadVersion(7)) # 3