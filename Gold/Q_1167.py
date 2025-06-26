from collections import deque

N = int(input())
A = [[] for _ in range(N + 1)]

for _ in range(N):
    Arr = list(map(int, input().split()))
    i = 0
    S = Arr[i]
    i += 1
    while True:
        E = Arr[i]
        if E == -1:
            break
        V = Arr[i + 1]
        A[S].append((E, V))
        i += 2

distance = [0] * (N + 1)
visited = [False] * (N + 1)

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now = queue.popleft()
        for pair in A[now]:
            if not visited[pair[0]]:
                visited[pair[0]] = True
                queue.append(pair[0])
                distance[pair[0]] = distance[now] + pair[1]

BFS(1)
Max = 1
for i in range(2, N + 1):
    if distance[i] > distance[Max]:
        Max = i
        
distance = [0] * (N + 1)
visited = [False] * (N + 1)
BFS(Max)
print(max(distance))