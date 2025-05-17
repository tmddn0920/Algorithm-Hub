from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    graph[i].sort()

visited = [False] * (n + 1)

def dfs(x):
    visited[x] = True
    print(x, end=' ')
    for i in graph[x]:
        if not visited[i]:
            dfs(i)

dfs(v)
print()

visited = [False] * (n + 1)

def bfs(x):
    q = deque([x])
    visited[x] = True
    while q:
        cur = q.popleft()
        print(cur, end=' ')
        for i in graph[cur]:
            if not visited[i]:
                visited[i] = True
                q.append(i)

bfs(v)