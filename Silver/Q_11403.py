N = int(input())
A = []

for _ in range(N):
    A.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        for k in range(N):
            if A[j][i] == 1 and A[i][k] == 1:
                A[j][k] = 1
                
for i in range(N):
    for j in range(N):
        print(A[i][j], end = " ")
    print()