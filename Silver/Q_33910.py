N = int(input())
A = list(map(int, input().split()))

Min = A[-1]

for i in range(N - 2, -1, -1):
    if A[i] > Min:
        A[i] = Min
    else:
        Min = A[i]

print(sum(A))
