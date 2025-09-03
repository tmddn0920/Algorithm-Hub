from collections import deque

N, R, Q = map(int, input().split())
A = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    U, V = map(int, input().split())
    A[U].append(V)
    A[V].append(U)
    
parent = [0] * (N + 1)
total = [0] * (N + 1)

queue = deque([R])
order = []
parent[R] = -1

while queue:
    temp = queue.pop()
    order.append(temp)
    for i in A[temp]:
        if i == parent[temp]:
            continue
        parent[i] = temp
        queue.append(i)
        
for i in reversed(order):
    total[i] = 1
    for j in A[i]:
        if j == parent[i]:
            continue
        total[i] += total[j]
        
for _ in range(Q):
    num = int(input())
    print(total[num])