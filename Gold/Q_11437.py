N = int(input())
tree = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    start, end = map(int, input().split())
    tree[start].append(end)
    tree[end].append(start)
    
tree_depth = [0] * (N + 1)
parent = [0] * (N + 1)
visited = [0] * (N + 1)

def BFS(n):
    queue = [n]
    visited[n] = True
    while queue:
        temp = queue.pop(0)
        for node in tree[temp]:
            if not visited[node]:
                visited[node] = True
                queue.append(node)
                parent[node] = temp
                tree_depth[node] = tree_depth[temp] + 1
                
BFS(1)

def findParent(a, b):
    if tree_depth[a] < tree_depth[b]:
        temp = a
        a = b
        b = temp
        
    while tree_depth[a] != tree_depth[b]:
        a = parent[a]
        
    while a != b:
        a = parent[a]
        b = parent[b]
    
    return a

M = int(input())
result = dict()
for _ in range(M):
    a, b = map(int, input().split())
    if not result.get((a, b), 0):
        result[(a, b)] = result[(b, a)] = findParent(a, b)
    print(result.get((a, b)))