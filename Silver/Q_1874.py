num = int(input())
result_stack = [int(input()) for _ in range(num)]  

num_stack = []   
stack = []      
position = 1     
isStack = True  

while result_stack:
    target = result_stack[0]
    while position <= target:
        num_stack.append(position)
        stack.append('+')
        position += 1
    if num_stack[-1] == target:
        num_stack.pop()
        result_stack.pop(0)
        stack.append('-')
    else:
        isStack = False
        break

if isStack:
    for op in stack:
        print(op)
else:
    print('NO')