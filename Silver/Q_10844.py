mod = 1000000000
N = int(input())
A = [[0] * 11 for _ in range(N + 1)]

for i in range(1, 10):
    A[1][i] = 1
    
for i in range(2, N + 1):
    A[i][0] = A[i - 1][1]
    A[i][9] = A[i - 1][8]
    for j in range(1, 9):
        A[i][j] = A[i - 1][j - 1] + A[i - 1][j + 1]

result = 0
for i in range(0, 10):
    result += A[N][i]
    
print(result % mod)