infix = input()
op = []
postfix = ''
for i in infix:
    if i.isalpha():
        postfix += i
    else:
        if i == '(':
            op.append(i)
        elif i == '*' or i == '/':
            while op and (op[-1] == '*' or op[-1] == '/'):
                postfix += op.pop()
            op.append(i)
        elif i == '+' or i == '-':
            while op and op[-1] != '(':
                postfix += op.pop()
            op.append(i)
        else:
            while op and op[-1] != '(':
                postfix += op.pop()
            op.pop()

while op:
    postfix += op.pop()

print(postfix)
