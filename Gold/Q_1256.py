N, M, K = map(int, input().split())
A = [[0] * 202 for _ in range(202)]

for i in range(0, 201):
    for j in range(0, i + 1):
        if j == 0 or j == i:
            A[i][j] = 1
        else:
            A[i][j] = A[i - 1][j] + A[i - 1][j - 1]
            if A[i][j] > 1000000000:
                A[i][j] = 10000000001
                
if A[N + M][M] < K:
    print(-1)
else:
    while not (N == 0 and M == 0):
        if A[N - 1 + M][M] >= K:
            print('a', end ="")
            N -= 1
        else:
            print('z', end="")
            K -= A[N - 1 + M][M]
            M -= 1