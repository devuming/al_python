import re

# 이메일 추출
target = """hello_u@naver.com   abcd@yahoo.co.kr 
abcd_ss@daum.net youmny910@naver.com
a*@naver.com
aaaaaa__
ABC@naver.com
hello_u@naver_com
"""

regex = "\w+@[a-z]+.[a-z.]+"
result = re.findall(regex, target)
print('\n'.join(result))
print('---------------')

# 이메일 주소 [.] 주의!
regex = "\w+@[a-z]+[.][a-z.]+"
result = re.findall(regex, target)
print('\n'.join(result))

# 이메일 유효성 검사
print('---------------')
print(re.match(regex, target))
print(bool(re.match(regex, "hi@naver.com")))
print(bool(re.match(regex, "!hello**@naver.com")))
