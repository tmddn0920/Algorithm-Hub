from collections import deque

N = int(input())
tree = [[0] for _ in range(N + 1)]

for _ in range(N - 1):
    start, end = map(int, input().split())
    tree[start].append(end)
    tree[end].append(start)
    
depth = [0] * (N + 1)
visited = [False] * (N + 1)
temp = 1
k_limit = 0

while temp <= N:
    temp <<= 1
    k_limit += 1

parent = [[0] * (N + 1) for _ in range(k_limit + 1)]

def BFS(node):
    queue = deque()
    queue.append(node)
    visited[node] = True
    level = 1
    size = 1
    count = 0
    while queue:
        temp = queue.popleft()
        for next in tree[temp]:
            if not visited[next]:
                visited[next] = True
                queue.append(next)
                parent[0][next] = temp
                depth[next] = level
        count += 1
        if count == size:
            count = 0
            size = len(queue)
            level += 1

BFS(1)

for k in range(1, k_limit + 1):
    for n in range(1, N + 1):
        parent[k][n] = parent[k - 1][parent[k - 1][n]]
        
def LCA(a, b):
    if depth[a] > depth[b]:
        temp = a
        a = b
        b = temp
    
    for k in range(k_limit, -1, -1):
        if depth[b] - depth[a] >= (1 << k):
            if depth[parent[k][b]] >= depth[a]:
                b = parent[k][b]

    for k in range(k_limit, -1, -1):
        if a == b:
            break
        if parent[k][a] != parent[k][b]:
            a = parent[k][a]
            b = parent[k][b]
            
    result = a
    if a != b:
        result = parent[0][result]
    return result
    
M = int(input())

for _ in range(M):
    a, b = map(int, input().split())
    print(LCA(a, b))