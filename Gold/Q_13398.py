N = int(input())
A = list(map(int, input().split()))

Left = [0] * N
Right = [0] * N

Left[0] = A[0]
result = Left[0]
for i in range(1, N):
    Left[i] = max(A[i], Left[i - 1] + A[i])
    result = max(result, Left[i])

Right[N - 1] = A[N - 1]
for i in range(N - 2, -1, -1):
    Right[i] = max(A[i], Right[i + 1] + A[i])
    
for i in range(1, N - 1):
    temp = Left[i - 1] + Right[i + 1]
    result = max(result, temp)
    
print(result)