import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
    if x < 0 or y < 0 or x >= M or y >= N:
        return
    if farm[y][x] == 1:
        farm[y][x] = 0
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    farm = [[0]* M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        farm[y][x] = 1
    count = 0
    for y in range(N):
        for x in range(M):
            if farm[y][x] == 1:
                dfs(x, y)
                count += 1
    print(count)