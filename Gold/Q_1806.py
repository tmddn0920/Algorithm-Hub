N, S = map(int, input().split())
A = list(map(int, input().split()))

result = N + 1
total = 0
l = 0

for r in range(N):
    total += A[r]
    while total >= S:
        length = r - l + 1
        if length < result:
            result = length
        total -= A[l]
        l += 1
        
if result == N + 1:
    print(0)
else:
    print(result)