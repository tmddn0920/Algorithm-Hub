import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, M = map(int, input().split())
A = [[] for _ in range(N)]
visited = [False] * N
result = False
for _ in range(M):
    a, b = map(int, input().split())
    A[a].append(b)
    A[b].append(a)

def dfs(num, depth):
    global result
    if depth == 5:
        result = True
        return
    visited[num] = True
    for i in A[num]:
        if not visited[i]:
            dfs(i, depth + 1)
    visited[num] = False
    
for i in range(N):
    dfs(i, 1)
    if result:
        break

if result:
    print(1)
else:
    print(0)