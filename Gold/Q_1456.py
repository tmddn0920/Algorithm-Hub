import math
Min, Max = map(int, input().split())
A = [0] * 10000001

for i in range(2, 10000001):
    A[i] = i

for i in range(2, int(math.sqrt(10000001) + 1)):
    if A[i] == 0:
        continue
    for j in range(i * 2, 10000001, i):
        A[j] = 0

result = 0

for i in range(2, 10000001):
    if A[i] != 0:
        temp = A[i]
        while A[i] <= Max / temp:
            if A[i] >= Min / temp:
                result += 1
            temp = temp * A[i]

print(result)