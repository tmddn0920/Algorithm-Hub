num = int(input())
for i in range(num):
    isRight = True
    line = input()
    stack = []
    for i in range(0, len(line)):
        if line[i] == '(':
            stack.append(line[i])
        if line[i] == ')':
            if not stack or stack[-1] == ')':
                isRight = False
                break
            stack.pop()
    if not stack and isRight == True:
        print('YES')
    else:
        print('NO')