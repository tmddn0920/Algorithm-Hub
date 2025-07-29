A = list(input())
B = list(input())

Matrix = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
result = []

for i in range(1, len(A) + 1):
    for j in range(1, len(B) + 1):
        if A[i - 1] == B[j - 1]:
            Matrix[i][j] = Matrix[i - 1][j - 1] + 1
        else:
            Matrix[i][j] = max(Matrix[i][j - 1], Matrix[i - 1][j])
            
print(Matrix[len(A)][len(B)])

def LCS(y, x):
    if y == 0 or x == 0:
        return
    if A[y - 1] == B[x - 1]:
        result.append(A[y - 1])
        LCS(y - 1, x - 1)
    else:
        if Matrix[y - 1][x] > Matrix[y][x - 1]:
            LCS(y - 1, x)
        else:
            LCS(y, x - 1)
            
LCS(len(A), len(B))
result.reverse()

for i in range(len(result)):
    print(result[i], end ="")