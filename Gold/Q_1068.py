import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

N = int(input())
visited = [False] * N
tree = [[] for _ in range(N)]
result = 0
root = 0
parent = list(map(int, input().split()))

for i in range(N):
    if parent[i] == -1:
        root = i
    else:
        tree[i].append(parent[i])
        tree[parent[i]].append(i)
        
remove_num = int(input())

def DFS(v):
    global result
    count = 0
    visited[v] = True
    for i in tree[v]:
        if visited[i] == False and i != remove_num:
            count += 1
            DFS(i)
    if count == 0:
        result += 1
        
if remove_num == root:
    print(0)
else:
    DFS(root)
    print(result)