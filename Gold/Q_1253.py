N = int(input())
A = list(map(int, input().split()))
result = 0
A.sort()

for k in range(N):
    i = 0
    j = N - 1
    while j > i:
        if A[i] + A[j] == A[k]:
            if i != k and j != k:
                result += 1
                break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1
        elif A[i] + A[j] > A[k]:
            j -= 1
        elif A[i] + A[j] < A[k]:
            i += 1
            
print(result)