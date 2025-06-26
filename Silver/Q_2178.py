from collections import deque 

N, M = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int, list(input()))))
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
visited = [[False] * M for _ in range(N)]

def BFS(i, j):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True
    while queue:
        location = queue.popleft()
        for k in range(4):
            x = location[0] + dx[k]
            y = location[1] + dy[k]
            if x >= 0 and y >= 0 and x < N and y < M:
                if A[x][y] > 0 and not visited[x][y]:
                    visited[x][y] = True
                    A[x][y] = A[location[0]][location[1]] + 1
                    queue.append((x, y))
BFS(0, 0)
print(A[N - 1][M - 1])                    