from collections import deque
N, M = map(int, input().split())
A = [[] for _ in range(N + 1)]
degree = [0] * (N + 1)

for _ in range(M):
    S, E = map(int, input().split())
    A[S].append(E)
    degree[E] += 1
    
queue = deque()

for i in range(1, N + 1):
    if degree[i] == 0:
        queue.append(i)
        
while queue:
    temp = queue.popleft()
    print(temp, end = " ")
    for i in A[temp]:
        degree[i] -= 1
        if degree[i] == 0:
            queue.append(i)