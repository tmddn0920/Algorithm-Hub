import sys
input = sys.stdin.readline

num = int(input())
queue = []

def push(x):
    queue.append(x)

def pop():
    if queue:
        print(queue.pop(0))
    else:
        print(-1)

def size():
    print(len(queue))

def empty():
    print(0 if queue else 1)

def front():
    if queue:
        print(queue[0])
    else:
        print(-1)
        
def back():
    if queue:
        print(queue[-1])
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
    elif line == 'front':
        front()
    elif line == 'back':
        back()
