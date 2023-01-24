# palindrom 문자열인지 아닌지 리턴하는 알고리즘
import re

def isPalindrome(s):
    s = s.lower()
    s = re.sub('[^a-z0-9]','',s)

    return s == s[::-1]

print(isPalindrome("A man, a plan, a canal: Panama"))       # True
print(isPalindrome("race a car"))   # False
print(isPalindrome(" "))    # True
print(isPalindrome("0P"))   # False