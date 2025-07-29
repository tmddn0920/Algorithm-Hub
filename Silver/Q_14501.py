N = int(input())
A = [0] * (N + 2)
T = [0] * (N + 1)
P = [0] * (N + 1)

for i in range(1, N + 1):
    T[i], P[i] = map(int, input().split())

for i in range(N, 0, -1):
    if i + T[i] > N + 1:
        A[i] = A[i + 1]
    else:
        A[i] = max(A[i + 1], P[i] + A[i + T[i]])
        
print(A[i])