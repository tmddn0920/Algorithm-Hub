import sys
sys.setrecursionlimit(10000)
sys.stdin.readline

N, M = map(int, input().split())
A = [[] for _ in range(N + 1)]
Visited = [False] * (N + 1)
count = 0

def dfs(v):
    Visited[v] = True
    for u in A[v]:
        if not Visited[u]:
            dfs(u)

for _ in range(M):
    u, v = map(int, input().split())
    A[u].append(v)
    A[v].append(u)
    
for v in range(1, N + 1):
    if not Visited[v]:
        dfs(v)
        count += 1

print(count)