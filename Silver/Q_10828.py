import sys
input = sys.stdin.readline

num = int(input())
stack = []

def push(x):
    stack.append(x)

def pop():
    if stack:
        print(stack.pop())
    else:
        print(-1)

def size():
    print(len(stack))

def empty():
    print(0 if stack else 1)

def top():
    if stack:
        print(stack[-1])
    else:
        print(-1)

for _ in range(num):
    line = input().strip()
    if line.startswith('push'):
        _, x = line.split()
        push(int(x))
    elif line == 'pop':
        pop()
    elif line == 'size':
        size()
    elif line == 'empty':
        empty()
    elif line == 'top':
        top()
