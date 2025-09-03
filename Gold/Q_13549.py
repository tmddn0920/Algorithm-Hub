from collections import deque
import sys
input = sys.stdin.readline

def bfs(N, K):
    MAX = 100000
    A = [-1] * (MAX + 1) 
    q = deque()
    q.append(N)
    A[N] = 0

    while q:
        x = q.popleft()
        if x == K:
            return A[x]


        nx = x * 2
        if 0 <= nx <= MAX and (A[nx] == -1 or A[nx] > A[x]):
            A[nx] = A[x]
            q.appendleft(nx)  

        for nx in (x - 1, x + 1):
            if 0 <= nx <= MAX and (A[nx] == -1 or A[nx] > A[x] + 1):
                A[nx] = A[x] + 1
                q.append(nx) 

N, K = map(int, input().split())
print(bfs(N, K))
