import sys

N = int(input())

if N < 2:
    print(0)
    sys.exit(0)
    
isPrime = [True] * (N + 1)
isPrime[0] = isPrime[1] = False
for i in range(2, int(N ** 0.5) + 1):
    if isPrime[i]:
        for j in range(i * i, N + 1, i):
            isPrime[j] = False
A = [i for i in range(2, N + 1) if isPrime[i]]

count = 0
total = 0
l = 0
for r in range(len(A)):
    total += A[r]
    while total > N and l <= r:
        total -= A[l]
        l += 1
    if total == N:
        count += 1

print(count)