from collections import deque
import sys
input = sys.stdin.readline

MAX = 100000
N, K = map(int, input().split())

A = [-1] * (MAX + 1)       
parent = [-1] * (MAX + 1)  

def bfs(N, K):
    if N == K:
        print(0)
        print(N)
        return

    queue = deque()
    queue.append(N)
    A[N] = 0
    parent[N] = N

    while queue:
        temp = queue.popleft()
        if temp == K:
            break

        for nx in (temp - 1, temp + 1, temp * 2):
            if 0 <= nx <= MAX and A[nx] == -1:
                A[nx] = A[temp] + 1
                parent[nx] = temp
                queue.append(nx)

    path = []
    temp = K
    while True:
        path.append(temp)
        if temp == parent[temp]:
            break
        temp = parent[temp]
    path.reverse()

    print(A[K])
    for x in path:
        print(x, end=" ")

bfs(N, K)