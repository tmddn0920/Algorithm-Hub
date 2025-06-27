from collections import deque 

N, M = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
visited = [[False] * M for _ in range(N)]
distance = [[-1] * M for _ in range(N)]

def BFS(i, j):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True
    distance[i][j] = 0
    while queue:
        location = queue.popleft()
        for k in range(4):
            x = location[0] + dx[k]
            y = location[1] + dy[k]
            if x >= 0 and y >= 0 and x < N and y < M:
                if A[x][y] == 1 and not visited[x][y]:
                    visited[x][y] = True
                    distance[x][y] = distance[location[0]][location[1]] + 1
                    queue.append((x, y))
                    
for i in range(N):
    for j in range(M):
        if A[i][j] == 2:
            BFS(i, j)

for i in range(N):
    for j in range(M):
        if A[i][j] == 0:
            print(0, end=' ')
        else:
            print(distance[i][j], end=' ')
    print()