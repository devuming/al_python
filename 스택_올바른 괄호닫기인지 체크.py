# 올바른 괄호닫기인지 체크
def check_correct_str(s):
    stk = []
    for i in range(len(s)):
        if s[i] == '(':
            stk.append(s[i])
            continue
        if len(stk) == 0 or stk.pop() == ')':
            return False
        
    return len(stk) == 0
print(check_correct_str('(())'))        # T
print(check_correct_str(')('))          # F
print(check_correct_str(')))((('))      # F
print(check_correct_str(')())'))        # F
print(check_correct_str('(()())'))      # T
print(check_correct_str('(()))'))       # F
print(check_correct_str('(()('))        # F