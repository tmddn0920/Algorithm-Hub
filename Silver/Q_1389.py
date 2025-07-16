import sys

N, M = map(int, input().split())
A = [[sys.maxsize] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    A[i][i] = 0
    
for _ in range(M):
    start, end = map(int, input().split())
    A[start][end] = 1
    A[end][start] = 1
    
for i in range(1, N + 1):
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            if A[j][k] > A[j][i] + A[i][k]:
                A[j][k] = A[j][i] + A[i][k]
                
num = sys.maxsize
result = -sys.maxsize

for i in range(1, N + 1):
    total = 0
    for j in range(1, N + 1):
        total += A[i][j]
    if num > total:
        num = total
        result = i
        
print(result)