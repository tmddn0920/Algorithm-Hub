n, m = map(int, input().split())

A = list(map(int, input().split()))
S = [0] * n
R = [0] * m
count = 0

S[0] = A[0]
for i in range(1, n):
    S[i] = S[i - 1] + A[i]

for i in range(n):
    remain = S[i] % m
    if remain == 0:
        count += 1
    R[remain] += 1

for i in range(m):
    if R[i] > 1:
        count += R[i] * (R[i] - 1) // 2
        
print(count)
    
    