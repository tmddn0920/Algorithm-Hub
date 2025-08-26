from collections import deque

A = [-1] * (100001)
count = 0

N, K = map(int, input().split())

def bfs(N, K):
    q = deque()
    q.append(N)
    A[N] = 0
    
    while q:
        x = q.popleft()
        if x == K:
            return A[x]
        for i in (x -1, x + 1, x * 2):
            if 0 <= i <= 100000 and A[i] == -1:
                A[i] = A[x] + 1
                q.append(i)
                
print(bfs(N, K))