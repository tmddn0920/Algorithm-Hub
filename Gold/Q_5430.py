from collections import deque

T = int(input())

for _ in range(T):
    isReverse = False
    isError = False
    P = list(input())
    N = int(input())
    raw = input().strip()[1:-1]
    if raw == "":
        A = []
    else:
        A = list(map(int, raw.split(',')))
    dq = deque()
    dq.extend(A)
    for function in P:
        if function == 'R':
            isReverse = not isReverse
        elif function == 'D':
            if len(dq) == 0:
                isError = True
                break
            elif isReverse:
                dq.pop()
            elif not isReverse:
                dq.popleft()
    if isError:
        print('error')
    else:
        if isReverse:
            dq.reverse()
        print('[' + ','.join(map(str, dq)) + ']')