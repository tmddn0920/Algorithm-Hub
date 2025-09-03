from collections import deque
import sys
input = sys.stdin.readline

MAX = 100000
N, K = map(int, input().split())

A = [-1] * (MAX + 1)
C = [0] * (MAX + 1)

def bfs(N, K):
    if N == K:
        return 0, 1

    queue = deque()
    queue.append(N)
    A[N] = 0
    C[N] = 1

    while queue:
        temp = queue.popleft()

        for nx in (temp - 1, temp + 1, temp * 2):
            if 0 <= nx <= MAX:
                if A[nx] == -1:
                    A[nx] = A[temp] + 1
                    C[nx] = C[temp]
                    queue.append(nx)
                elif A[nx] == A[temp] + 1:
                    C[nx] += C[temp]

    return A[K], C[K]

time, count = bfs(N, K)
print(time)
print(count)