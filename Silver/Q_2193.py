N = int(input())
A = [[0] * 2 for _ in range(N + 1)]
A[1][1] = 1
A[1][0] = 0

for i in range(2, N + 1):
    A[i][0] = A[i - 1][1] + A[i - 1][0]
    A[i][1] = A[i - 1][0]
    
print(A[N][0] + A[N][1])