from collections import deque

T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    visited = [False] * 10000
    parent = [-1] * 10000
    op = [''] * 10000
    queue = deque()
    queue.append(A)
    visited[A] = True
    while queue:
        temp = queue.popleft()
        if temp == B:
            break
        else:
            num = (temp * 2) % 10000
            if visited[num] == False:
                visited[num] = True
                parent[num] = temp
                op[num] = 'D'
                queue.append(num)
            num = (temp + 9999) % 10000
            if visited[num] == False:
                visited[num] = True
                parent[num] = temp
                op[num] = 'S'
                queue.append(num)
            num = (temp % 1000) * 10 + (temp // 1000)
            if visited[num] == False:
                visited[num] = True
                parent[num] = temp
                op[num] = 'L'
                queue.append(num)
            num = (temp % 10) * 1000 + (temp // 10)
            if visited[num] == False:
                visited[num] = True
                parent[num] = temp
                op[num] = 'R'
                queue.append(num)
    path = []
    temp = B
    while temp != A:
        path.append(op[temp])
        temp = parent[temp]
    print(''.join(reversed(path)))