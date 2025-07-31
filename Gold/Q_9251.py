import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
A = list(input())
A.pop()
B = list(input())
B.pop()

Matrix = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
result = []

for i in range(1, len(A) + 1):
    for j in range(1, len(B) + 1):
        if A[i - 1] == B[j - 1]:
            Matrix[i][j] = Matrix[i - 1][j - 1] + 1
        else:
            Matrix[i][j] = max(Matrix[i][j - 1], Matrix[i - 1][j])
            
print(Matrix[len(A)][len(B)])