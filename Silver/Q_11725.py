import sys
sys.setrecursionlimit(100000)

N = int(input())
visited = [False] * (N + 1)
tree = [[] for _ in range(N + 1)]
parent = [0] * (N + 1)

for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def DFS(v):
    visited[v] = True
    for i in tree[v]:
        if visited[i] == False:
            parent[i] = v
            DFS(i)

DFS(1)

for i in range(2, N + 1):
    print(parent[i])