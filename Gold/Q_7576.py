from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

dirs = [(1,0), (-1,0), (0,1), (0,-1)]
queue = deque()

for y in range(N):
    for x in range(M):
        if A[y][x] == 1:
            queue.append((y, x))

level = -1
isValid = True

while queue:
    for _ in range(len(queue)):
        y, x = queue.popleft()
        for dy, dx in dirs:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M:
                if A[ny][nx] == 0:
                    A[ny][nx] = 1
                    queue.append((ny, nx))
    level += 1

for y in range(N):
    for x in range(M):
        if A[y][x] == 0:
            isValid = False

if isValid:
    print(level)
else:
    print(-1)