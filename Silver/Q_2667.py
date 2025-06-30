N = int(input())
A = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
for _ in range(N):
    A.append(list(input()))
Visited = [[False] * N for _ in range(N)]
Current = 1

def dfs(y, x):
    Visited[y][x] = True
    A[y][x] = Current
    for i in range(4):
        if 0 <= y + dy[i] < N and 0 <= x + dx[i] < N:
            if A[y + dy[i]][x + dx[i]] == '1' and not Visited[y + dy[i]][x + dx[i]]:
                Visited[y + dy[i]][x + dx[i]] = True
                A[y + dy[i]][x + dx[i]] = Current
                dfs(y + dy[i], x + dx[i])

for y in range(N):
    for x in range(N):
        if A[y][x] == '1' and not Visited[y][x]:
            dfs(y, x)
            Current += 1
 
Result = [0] * (Current - 1)

for y in range(N):
    for x in range(N):
        if A[y][x] != '0':
            Result[A[y][x] - 1] += 1

print(Current - 1)
Result.sort()
for num in Result:
   print(num) 
                
    