N, M = map(int, input().split())
Matrix_A = []
for _ in range(N):
    Matrix_A.append(list(map(int, input().split())))
    
M, K = map(int, input().split())
Matrix_B = []
for _ in range(M):
    Matrix_B.append(list(map(int, input().split())))

def Matrix_Mul(x, y):
    result = 0
    for num in range(M):
        result += Matrix_A[y][num] * Matrix_B[num][x]
    return result
 
Result_Arr = [[0] * K for _ in range(N)]

for y in range(N):
    for x in range(K):
        Result_Arr[y][x] = Matrix_Mul(x, y)

for row in Result_Arr:
    for num in row:
        print(num, end=" ")
    print()