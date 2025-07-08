import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
A = [[] for _ in range(N + 1)]
result = [0] * (N + 1)

def BFS(v):
    visited = [False] * (N + 1)
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        temp = queue.popleft()
        for i in A[temp]:
            if visited[i] == False:
                visited[i] = True
                result[i] += 1
                queue.append(i)

for _ in range(M):
    S, E = map(int, input().split())
    A[S].append(E)
        
for i in range(1, N + 1):
    BFS(i)

Max = max(result)

for i in range(1, N + 1):
    if result[i] == Max:
        print(i, end = " ")