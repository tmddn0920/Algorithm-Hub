import sys
input = sys.stdin.readline
from collections import deque

N, M, K, X = map(int, input().split())
A = [[] for _ in range(N + 1)]
result = []
visited = [-1] * (N + 1)

def DFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = 0
    while queue:
        temp = queue.popleft()
        for i in A[temp]:
            if visited[i] == -1:
                visited[i] = visited[temp] + 1
                queue.append(i)

for _ in range(M):
    S, E = map(int, input().split())
    A[S].append(E)
    
DFS(X)

for i in range(1, N + 1):
    if visited[i] == K:
        result.append(i)
        
result.sort()

if len(result) == 0:
    print(-1)
else:
    for i in range(len(result)):
        print(result[i])