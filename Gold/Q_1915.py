Matrix = [[0] * 1001 for _ in range(1001)]
N, M = map(int, input().split())
result = 0

for i in range(N):
    A = list(input())
    for j in range(M):
        Matrix[i][j] = int(A[j])
        if Matrix[i][j] == 1 and i > 0 and j > 0:
            Matrix[i][j] = min(Matrix[i - 1][j - 1], Matrix[i - 1][j], Matrix[i][j - 1]) + Matrix[i][j]
        if result < Matrix[i][j]:
            result = Matrix[i][j]
            
print(result * result)