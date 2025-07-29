N, K = map(int, input().split())
A = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(N + 1):
    A[i][0] = 1
    A[i][i] = 1
    A[i][1] = i
    
for i in range(2, N + 1):
    for j in range(1, i):
        A[i][j] = A[i - 1][j] + A[i - 1][j - 1]
        A[i][j] = A[i][j] % 10007
        
print(A[N][K])