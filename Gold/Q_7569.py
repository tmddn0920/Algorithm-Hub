from collections import deque

M, N, H = map(int, input().split())
A = [[[-1 * M] for _ in range(N)] for _ in range(H)]
direction = [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]
level = -1
isValid = True

for i in range(N * H):
    A[i // N][i % N] = list(map(int, input().split()))

queue = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if A[i][j][k] == 1:
                queue.append((i, j, k))
                
while queue:
    for _ in range(len(queue)):
        z, y, x = queue.popleft()
        for dz, dy, dx in direction:
            nz, ny, nx = z + dz, y + dy, x + dx
            if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M:
                if A[nz][ny][nx] == 0:
                    A[nz][ny][nx] = 1
                    queue.append((nz, ny, nx))
    level += 1

for i in range(H):
    for j in range(N):
        for k in range(M):
            if A[i][j][k] == 0:
                isValid = False
                
if isValid:
    print(level)
else:
    print(-1)