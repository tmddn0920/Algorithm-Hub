import sys
sys.setrecursionlimit(100000)
K = int(input())
result = True

def DFS(v):
    global result
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            check[i] = (check[v] + 1) % 2
            DFS(i)
        elif check[v] == check[i]:
            result = False
            
for _ in range(K):
    V, E = map(int, input().split())
    A = [[] for _ in range(V + 1)]
    visited = [False] * (V + 1)
    check = [0] * (V + 1)
    result = True
    
    for _ in range(E):
        Start, End = map(int, input().split())
        A[Start].append(End)
        A[End].append(Start)
        
    for i in range(1, V + 1):
        DFS(i)
        
    if result:
        print('YES')
    elif not result:
        print('NO')