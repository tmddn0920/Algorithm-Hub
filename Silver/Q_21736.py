import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(input().rstrip()))  
Visited = [[False] * M for _ in range(N)]
Direction_X = [0, 1, 0, -1]
Direction_Y = [1, 0, -1, 0]
Count = 0

def bfs(x, y):
    global Count
    queue = deque()
    queue.append((x, y))
    Visited[y][x] = True

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in zip(Direction_X, Direction_Y):
            nx = cx + dx
            ny = cy + dy
            if 0 <= nx < M and 0 <= ny < N and not Visited[ny][nx]:
                if A[ny][nx] == 'O':
                    Visited[ny][nx] = True
                    queue.append((nx, ny))
                elif A[ny][nx] == 'P':
                    Count += 1
                    Visited[ny][nx] = True
                    queue.append((nx, ny))

for i in range(N):
    for j in range(M):
        if A[i][j] == 'I':
            bfs(j, i)

if Count > 0:
    print(Count)
else:
    print('TT')
