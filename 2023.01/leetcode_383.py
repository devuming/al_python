# leetcode 383.Ransom Note
# 두 개의 문자열 ransomNote과 magazine이 주어졌을 때, ransomNote이 magazine이의 문자를 사용하여 구성될 수 있다면 true를 반환하고 그렇지 않으면 false를 반환한다.

# magazine의 각 문자는 ransomNote에서 한 번만 사용할 수 있습니다.
from collections import Counter
def canConstruct(ransomNote, magazine):
    d_mag = Counter(list(magazine))

    for r in ransomNote:
        if d_mag.get(r, 0) > 0:
            d_mag[r] = d_mag.get(r, 0) - 1
        else:
            return False
    return True

print(canConstruct('a', 'b'))       # false
print(canConstruct('aa', 'ab'))     # false
print(canConstruct('aa', 'aab'))    # True
print(canConstruct('ac', 'aabbcc'))    # True
print(canConstruct('acc', 'aabbcc'))    # True
print(canConstruct('acce', 'aabbcc'))    # false
print(canConstruct('accc', 'aabbcc'))    # false
print(canConstruct('abac', 'aabbcc'))    # True