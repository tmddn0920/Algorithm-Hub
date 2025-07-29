A = [0] * 51
P = [0] * 51
M = int(input())
A = list(map(int, input().split()))
K = int(input())
Total = 0

for i in range(0, M):
    Total += A[i]

result = 0

for i in range(0, M):
    if A[i] >= K:
        P[i] = 1
        for j in range(0, K):
            P[i] = P[i] * (A[i] - j) / (Total - j)
        result += P[i]
        
print(result)