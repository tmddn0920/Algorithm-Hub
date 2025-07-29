N = int(input())
mod = 1000000000
A = [0] * 1000001
A[1] = 0
A[2] = 1

for i in range(3, N + 1):
    A[i] = (i - 1) * (A[i - 1] + A[i - 2]) % mod

print(A[N])