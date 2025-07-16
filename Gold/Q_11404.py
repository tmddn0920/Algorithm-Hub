import sys

N = int(input())
M = int(input())
A = [[sys.maxsize] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    A[i][i] = 0
    
for i in range(M):
    start, end, weight = map(int, input().split())
    if A[start][end] > weight:
        A[start][end] = weight

for i in range(1, N + 1):
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            if A[j][k] > A[j][i] + A[i][k]:
                A[j][k] = A[j][i] + A[i][k]
                
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if A[i][j] == sys.maxsize:
            print(0, end = " ")
        else:
            print(A[i][j], end = " ")
    print()