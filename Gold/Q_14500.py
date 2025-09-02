import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
dr_x = [1, 0, -1, 0]
dr_y = [0, 1, 0, -1]

result = 0

def dfs(x, y, depth, total):
    global result
    if depth == 4:
        result = max(result, total)
        return

    for d in range(4):
        nx = x + dr_x[d]
        ny = y + dr_y[d]
        if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx]:
            visited[ny][nx] = True
            dfs(nx, ny, depth + 1, total + A[ny][nx])
            visited[ny][nx] = False

def not_dfs(y, x):
    global result
    cordinate = []
    for d in range(4):
        nx = x + dr_x[d]
        ny = y + dr_y[d]
        if 0 <= nx < M and 0 <= ny < N:
            cordinate.append(A[ny][nx])
    if len(cordinate) >= 3:
        cordinate.sort(reverse=True)
        result = max(result, A[y][x] + sum(cordinate[:3]))

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(j, i, 1, A[i][j])
        visited[i][j] = False
        not_dfs(i, j)

print(result)