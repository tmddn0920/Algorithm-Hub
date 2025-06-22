A, B = map(str, input().split())
count = 0

if len(A) == len(B):
    for i in range(len(A)):
        if A[i] != B[i]:
            count += 1
    print(count)

Arr = []
if len(A) < len(B):
    for i in range(0, len(B) - len(A) + 1):
        num = 0
        for j in range(len(A)):
            if A[j] != B[i + j]:
                num += 1
        Arr.append(num)
    print(min(Arr))