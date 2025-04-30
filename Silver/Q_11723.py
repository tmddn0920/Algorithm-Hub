import sys
input = sys.stdin.readline

set = [0] * 20
num = int(input())

for i in range(num):
    line = input().split()
    if len(line) > 1:
        line[1] = int(line[1])
    if line[0] == 'add':
        if set[line[1] - 1] == 0:
            set[line[1] - 1] = 1
    elif line[0] == 'check':
        if set[line[1] - 1] == 1:
            print(1)
        else:
            print(0)
    elif line[0] == 'remove':
        if set[line[1] - 1] == 1:
            set[line[1] - 1] = 0
    elif line[0] == 'toggle':
        if set[line[1] - 1] == 0:
            set[line[1] - 1] = 1
        elif set[line[1] - 1] == 1:
            set[line[1] - 1] = 0
    elif line[0] == 'empty':
        set = [0] * 20
    elif line[0] == 'all':
        set = [1] * 20