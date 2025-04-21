num = int(input())
stack = []
for i in range(num):
    number = int(input())
    if number != 0:
        stack.append(number)
    if number == 0:
        stack.pop(-1)
result = 0
for i in range(len(stack)):
    result += stack[i]
print(result)